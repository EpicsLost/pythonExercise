import xlrd
import xlwt

name = "C://Users/hp/Desktop/16卓越成绩.xlsx"
bk = xlrd.open_workbook(name)
sheet = bk.sheet_by_index(0)
print(sheet.name)
print(sheet.ncols)
print(sheet.nrows)

data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))
print(data)

s = [68,85,102,51,89,6,34,68,48,51,68,51,67,32,34,6,18]
for i in range(len(data)-1):
    sum = int(data[i+1][2])*s[0]+int(data[i+1][3])*s[1]+int(data[i+1][4])*s[2]+int(data[i+1][5])*s[3]+int(data[i+1][6])*s[4]+int(data[i+1][7])*s[5]+int(data[i+1][8])*s[6]+int(data[i+1][9])*s[7]+int(data[i+1][10])*s[8]+int(data[i+1][11])*s[9]+int(data[i+1][12])*s[10]+int(data[i+1][13])*s[11]+int(data[i+1][14])*s[12]+int(data[i+1][15])*s[13]+int(data[i+1][16])*s[14]+int(data[i+1][17])*s[15]+int(data[i+1][18])*s[16]+int(data[i+1][19])*int(data[i+1][20])+int(data[i+1][21])*int(data[i+1][22])+int(data[i+1][23])*int(data[i+1][24])
    score = float(sum/(878+data[i+1][20]+data[i+1][22]+data[i+1][24]))
    data[i+1][25] = score


exc = xlwt.Workbook()
sheet1 = exc.add_sheet(u"排名")
sheet1.write(0,0,"名次")
for i in range(len(data)):
    sheet1.write(i+1, 0, i+1)
    sheet1.write(i, 1, data[i][1])
    sheet1.write(i, 2, data[i][25])
exc.save("C://Users/hp/Desktop/test.xls")