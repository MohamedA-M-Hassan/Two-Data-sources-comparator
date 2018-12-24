import pandas as pd
from xlwt import Workbook

# create file 

wb= Workbook()

sheet1 = wb.add_sheet('sheet 1')

file_ = pd.read_excel("GFS.xlsx","Sheet1")

# we should append all elements in the col to List we will need it at the check stage inside the algorithem 
GFS_CODE_List=[]
for cell in (file_['GFS_CODE']):
    GFS_CODE_List.append(cell)

# create second file 

wb2= Workbook()

sheet2 = wb2.add_sheet('sheet 1')

file_ = pd.read_excel("GFS2.xlsx","Sheet1")

# we should append all elements in the col to List we will need it atcell_file2 the check stage inside the algorithem 
GFS_CODE_List2=[]
for cell in (file_['GFS_CODE']):
    GFS_CODE_List2.append(cell)



flag = True

for cell_file1,cell_file2 in zip(GFS_CODE_List,GFS_CODE_List2):
	if cell_file1 != cell_file2:
		flag = False
		
print(flag)
