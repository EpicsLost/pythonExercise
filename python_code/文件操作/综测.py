import xlrd
import xlwt

name = "C://Users/hp/Desktop/6B430.xlsx"
bk = xlrd.open_workbook(name)
sheet = bk.sheet_by_index(0)
print(sheet.name)
print(sheet.ncols)
print(sheet.nrows)

data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))
print(data)

for i in range(len(data)-1):
    sum = data[i+1][2]*68+data[i+1][3]*85+data[i+1][4]*102+data[i+1][5]*51+data[i+1][6]*89+data[i+1][7]*6+data[i+1][8]*34+data[i+1][9]*68+data[i+1][10]*48+data[i+1][11]*51+data[i+1][12]*68+data[i+1][13]*51+data[i+1][14]*85+data[i+1][15]*32+data[i+1][16]*34+data[i+1][17]*6+data[i+1][18]*18+data[i+1][19]*data[i+1][20]+data[i+1][21]*data[i+1][22]+data[i+1][23]*data[i+1][24]
    score = float(sum/(896+data[i+1][20]+data[i+1][22]+data[i+1][24]))
    data[i+1][25] = score


exc = xlwt.Workbook()
sheet1 = exc.add_sheet(u"排名")
sheet1.write(0,0,"名次")
for i in range(len(data)):
    sheet1.write(i+1, 0, i+1)
    sheet1.write(i, 1, data[i][1])
    sheet1.write(i, 2, data[i][25])
exc.save("C://Users/hp/Desktop/test.xls")