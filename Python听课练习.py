# match case
# day = input("请输入星期几：")
# match day:
#     case "Monday":
#         print("星期一")
#     case "Tuesday":
#         print("星期二")
#     case "Wednesday":
#         print("星期三")
#     case "Thursday":
#         print("星期四")
#     case "Friday":
#         print("星期五")
#     case "Saturday":
#         print("星期六")
#     case "Sunday":
#         print("星期日")
#     case _:
#         print("输入有误")

# while循环
i = 0
while i < 10:
    print(i)
    i += 1
else:
    print("循环结束")

#计算1-100之间所有偶数的和
sum = 0 
for i in range(1, 101):
    if i % 2 == 0:
        sum += i    
print(sum)

sum = 0
while True:
    num = int(input("请输入一个整数（输入0结束）："))
    if num == 0:
        break
    sum += num
print("输入的整数的和为：", sum)
