## to deal with excel

import pandas as pd
from xlwt import Workbook

# create file 

wb= Workbook()
sheet1 = wb.add_sheet('sheet 1')
file1 = pd.read_excel("GFS.xlsx","Sheet1")

# create second file 
wb2= Workbook()
sheet2 = wb2.add_sheet('sheet 1')
file2 = pd.read_excel("GFS2.xlsx","Sheet1")

flag = True

for col_f1,col_f2 in zip(file1,file2):
	for cell_file1,cell_file2 in zip(file1[col_f1],file2[col_f2]):
		if cell_file1 != cell_file2:
			flag = False

print(flag)
