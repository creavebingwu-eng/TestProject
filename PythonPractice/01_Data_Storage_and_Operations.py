# 输入一个整数和一个表示数字的字符串，两个值相加后输出结果
input_int = int(input("请输入一个整数："))  # 输入的是字符串，使用 int() 转换为整数
input_str = input("请输入一个数字字符串：")  # 输入的是字符串
result = input_int + int(input_str)  # 使用 int() 将字符串转换为整数后相加
print("相加的结果是：", result)  # 输出整数类型的结果