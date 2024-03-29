### My very first python scripts from 2020/2021 for MALDI MS data processing  

_published:https://www.nature.com/articles/s41598-023-51021-3_

MALDI mass spectra were processed in FlexAnalysis software (Bruker) using a method created directly for permethylated glycans. 
First, the mass spectra baseline was subtracted (TopHat) and spectra were smoothed 
(SavitzkyGolay algorithm was used width 0.08 m/z; 5 cycles).  The peaklists were found with following parameters: SNAP was used as peak detection algorithm, 
with average compostion of (C1 O0.5 H1.6N0.05)nNa, S/N was set to 1 and quality factor threshold to 50. 
Overall, loose conditions were used to avoid leaving out low intensity glycans. 
The resulting peaklists were then searched against database using a python script written for this purpose (see Supporting information).
Individual masses in the database were iterated and signal intensity areas of corresponding peaks from peaklist were assigned to the database values. 
The first peak was searched within a mass window around reference masses  +- 0.2 Da, the mass error (ref. mass - measured mass/ref. mass) 
of the assigned peak was calculated and taken in account in ongoing database and peaklists iteration: the center of mass window 
was shifted by the mass error in order to compensate mass shift in the range of higher m/z. 
