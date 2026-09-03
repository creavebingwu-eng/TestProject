'''
# 列表示例：创建一个包含不同类型元素的列表
my_list = [1, "hello", 3.14, True]
print(my_list)
# 元组示例：创建一个包含不同类型元素的元组
my_tuple = (1, "world", 2.71, False)
print(my_tuple) 
# 字典示例：创建一个包含键值对的字典
my_dict = {"name": "Alice", "age": 30, "is_student": False}
print(my_dict)  
# 集合示例：创建一个包含唯一元素的集合
my_set = {1, 2, 3, 4, 5}
print(my_set)
'''

'''list练习1
# 将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序，输出其中的最小值、最大值、平均值
numbers = []# 创建一个空列表用于存储用户输入的数字

for i in range(10):  # 循环10次，获取用户输入的数字，range(10) 表示从 0 到 9 的整数序列
    num = float(input(f"请输入第 {i + 1} 个数字："))  # 获取用户输入的数字，并转换为浮点数，f字符串允许在字符串中嵌入表达式，使得字符串的格式化更加方便和直观
    numbers.append(num)  # 将输入的数字添加到列表中，numbers.append(num) 方法用于在列表末尾添加一个元素。
print("输入的数字列表：", numbers)  # 输出用户输入的数字列表

numbers.sort()  # 对列表中的数字进行排序

print("排序后的数字：", numbers)
print("最小值：", numbers[0])
print("最大值：", numbers[-1]) # 反向索引，-1 表示列表的最后一个元素
print("平均值：", sum(numbers) / len(numbers)) # 计算平均值，sum(numbers) 计算列表中所有数字的和，len(numbers) 获取列表中元素的数量
'''

'''list练习2
# 合并两个列表中的元素，去除重复元素后输出结果
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("直接合并的列表：", list1 + list2)  # 输出直接合并的列表，可能包含重复元素

merged_list = list(set(list1 + list2))  # 使用 set() 去除重复元素，然后再转换回列表
print("合并后的列表（去重）：", merged_list)  # 输出合并后的列表，去除重复元素后的结果 

for i in list2:
    if i in list1:
        continue  # 如果元素在 list1 中，则跳过当前循环，继续下一个元素
    list1.append(i)  # 如果元素不在 list1 中，则将其添加到 list1 中
print("合并后的列表（保留顺序）：", list1)  # 输出合并后的列表，保留顺序的结果

for i in list2:
    if i not in list1:  # 检查元素是否不在 list1 中
        list1.append(i)  # 如果元素不在 list1 中，则将其添加到 list1 中
print("合并后的列表（保留顺序）：", list1)  # 输出合并后的列表，保留顺序的结果
'''
'''list练习3
# 生成1-20的平方列表。从数字列表中提取所有偶数，并计算其平方，组成一个新的列表
squares = [x**2 for x in range(1, 21)]  # 使用列表推导式生成1到20的平方列表
even_squares = [x for x in squares if x % 2 == 0]  # 从平方列表中提取所有偶数，组成一个新的列表
print("1 到 20 的平方列表：", squares)  # 输出1到20的平方列表
print("平方列表中的偶数：", even_squares)  # 输出平方列表中的偶数列表
'''

# 邮箱格式验证：用户输入一个邮箱，验证其格式是否正确（包含@和.，且@在.之前）
email = input("请输入邮箱地址：")  # 获取用户输入的邮箱地址
if "@" in email and "." in email and email.index("@") < email.index("."):
    print("邮箱格式正确")
else:
    print("邮箱格式不正确")
# email.index用于获取指定字符在字符串中第一次出现的位置，如果@在.之前，则说明邮箱格式正确，否则格式不正确
# gmail的.可以在@之前，这个方法不太严谨
