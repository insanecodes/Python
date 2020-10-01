import xlwt 
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('sheet 1')

sheet1.write(1,0,'Rohan')
sheet1.write(2,0,'Rahul')
sheet1.write(3,0,'Subh')
sheet1.write(4,0,'Rajan')
sheet1.write(0,1,'Rohan')
sheet1.write(0,2,'Rahul')
sheet1.write(0,3,'subh')
sheet1.write(0,4,'Rajan')

wb.save('example.xls')