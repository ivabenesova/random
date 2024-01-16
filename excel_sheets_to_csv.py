import pandas as pd
 
print("reading file")
in_file = open("sada7.xlsx", "rb")
data = in_file.read() 
in_file.close()

all_sheets = pd.read_excel(data, sheet_name=None, header=None)
sheets = all_sheets.keys()

for sheet_name in all_sheets.keys():
    sheet = all_sheets[sheet_name] #pd.read_excel(data, sheet_name=sheet_name, header=None)
    title = sheet.loc[0,0]
    title_split = title.split("\\")[4]
    print(title_split)
    sheet.to_csv("csv/%s.csv" % title_split, index=False)

print("completed")