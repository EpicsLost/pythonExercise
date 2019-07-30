import xlrd
import xlwt

name = "C:/Users/hp/Desktop/中国大学排名.xls"
bk = xlrd.open_workbook(name)
sheet_name = bk.sheet_names()[0]
sheet = bk.sheet_by_index(0)
print(sheet.name)
print(sheet.ncols)
print(sheet.nrows)

data = []
for i in range(sheet.nrows):
    data.append(sheet.row_values(i))
print(data)

for i in range(len(data)-1):
    score = data[i+1][2]
    score = float(score)
    score = score+100
    data[i + 1][3] = score

print(data)
s = sorted(data[1:], key = lambda x:x[2],reverse=False)
print(s)

def save(data):
    exc = xlwt.Workbook()
    sheet1 = exc.add_sheet(u"排名")
    sheet1.write(0,0,"排名")
    sheet1.write(0,1,"名称")
    sheet1.write(0,2,"分数")
    for i in range(len(data)):
        sheet1.write(i + 1, 0, data[i][0])
        sheet1.write(i + 1, 1, data[i][1])
        sheet1.write(i + 1, 2, data[i][2])
        sheet1.write(i + 1, 3, data[i][3])
    exc.save("C:/Users/hp/Desktop/排名.xls")
save(s)



