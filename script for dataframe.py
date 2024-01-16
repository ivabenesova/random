import numpy as np
import pandas as pd
import csv
import sys
import glob
import os.path

#generates an empty list for collecting signal intensity areas of selected masses from individual mass spectra
glycan_table = []
#generates an list in which names of samples are collected
sample_names = ["ref_masses"]

#reads database csv file and generates a list of reference mass values 
database = pd.read_csv("database_final.csv", sep=";", header = 0 )
database_values = database["Basic"].tolist() 

#adds the list of the reference mass values as a first value in glycan_table
glycan_table.append(database_values)


list_of_files = glob.glob("csv/*.csv")
for file in sorted(list_of_files):
    #reads csv file with mass spectra peaklists and generates a list with mz values (masslist_mz) and a list with area values (masslist_area) 
    masslist_data = pd.read_csv(file, sep= ",", header = 3) 
    masslist_mz = masslist_data["m/z"].tolist()
    masslist_area = masslist_data["Area"].tolist()
    #generates the name from the name of the csv file (cuts the .csv suffix and first 5 characters), appends the name to sample_names list
    csv_name = file[4:-4]
    sample_names.append(csv_name)

    #variables needed 
    error1 = 0.2        #default mass error, in Da
    first_peak = 0  
    mass_error = 0
    window = 0.2        
    last_peak = 0
    stop_cycle = False
    glycan_list = []    #an empty list, in which signal intensity areas of masses corresponging to reference values will be later added 
    #fills the list with zeros
    for a in range(len(database_values)): 
        glycan_list.append(0)
    
    #search for the first peak:
    for ref_mass in database_values:
        ref_mass_index = database_values.index(ref_mass)
        for mz in masslist_mz:
            if ref_mass >= (mz - error1) and ref_mass < (mz + error1):
                #adds the peak to the glycan_list (replaces a zero on position corresponding to the ref_mass)
                mass_error = (mz - ref_mass)/ref_mass
                mz_index = masslist_mz.index(mz)
                mz_area = masslist_area[mz_index]
                glycan_list[ref_mass_index] = mz_area
                first_peak = ref_mass 
                stop_cycle = True
                last_peak = ref_mass
                break

        if stop_cycle == True:
            break
    #all the other masses   
    for ref_mass in database_values:
        ref_mass_index = database_values.index(ref_mass)
        if ref_mass > first_peak:
            for mz in masslist_mz:
                if (ref_mass >= (mz - (mz*mass_error) - window)) and (ref_mass <= (mz - (mz*mass_error) + window)) and mz > (last_peak + 0.5):
                    mass_error = (mz - ref_mass)/ref_mass
                    mz_index = masslist_mz.index(mz)
                    mz_area = masslist_area[mz_index]
                    glycan_list[ref_mass_index] = mz_area
                    last_peak = ref_mass
    
    glycan_table.append(glycan_list)

df_glycan_final = pd.DataFrame(glycan_table)
df_glycan_final = df_glycan_final.transpose()
df_glycan_final.columns = sample_names

#generates the final table as csv file
df_glycan_final.to_csv("results.csv", index = False)

