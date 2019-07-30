
product_list = [("华为",2999),
             ("小米",1999),
             ("苹果",6999)]

sal = input("请输入您的工资：")
shop_list = []
i = 0

if sal.isdigit():
    sal = int(sal)
    for item in product_list:
         print(i,item)
         i += 1
while True:
    num = input("请输入要购买的商品编号:")
    if num.isdigit():
        num = int(num)
        if num >=0 and num <len(product_list):
            print(product_list[num])
            if sal > product_list[num][1]:
                shop_list.append(product_list[num])
                sal =  sal - product_list[num][1]
                print("余额是%d"%sal)
            else:
                print("余额不够，无法购买！")
        else:
            print("并无此产品!")
    elif num == "q":
        print("您购买的商品如下：")
        for i in shop_list:
            print(i)
        exit()


