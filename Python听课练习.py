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
# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print("循环结束")

# #计算1-100之间所有偶数的和
# sum = 0 
# for i in range(1, 101):
#     if i % 2 == 0:
#         sum += i    
# print(sum)

# sum = 0
# while True:
#     num = int(input("请输入一个整数（输入0结束）："))
#     if num == 0:
#         break
#     sum += num
# print("输入的整数的和为：", sum)


#列表list
# s = [1, 2, 3, 4, 5]
# print(s[0])  # 输出第一个元素
# print(s[-1])  # 输出最后一个元素
# print(s[1:4])  # 输出第二个到第四个元素
# s.append(6)  # 在列表末尾添加一个元素
# print(s)  # 输出整个列表
# s.remove(3)  # 删除元素3
# #删除第一个元素
# s.pop(0)
# #删除最后一个元素
# s.pop(-1)
# del s[1]  # 删除第二个元素
# print(s)  # 输出整个列表
# #在指定位置添加元素
# s.insert(2, 100)
# print(s)  # 输出整个列表
# #清空列表
# s.clear()
# print(s)  # 输出空列表 []
#列表切片，开始索引为0，结束索引为4，步长为2
sl = [1, 2, 3, 4, 5]
print(sl[0:4:2])  # 输出 [1, 3]
print(sl[0:5:2])  # 输出 [1, 3, 5]

