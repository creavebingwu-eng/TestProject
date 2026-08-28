# 循环示例：计算 1 到 10 的整数和
sum_result = 0  # 初始化和为 0
for i in range(1, 11):  # 遍历 1 到 10 的整数
    sum_result += i  # 将当前整数加到和中
print("1 到 10 的整数和是：", sum_result)  # 输出结果

# 条件判断示例：判断一个数是正数、负数还是零
num = float(input("请输入一个数字："))
if num > 0:
    print("这是一个正数")
elif num < 0:
    print("这是一个负数")
else:
    print("这是零")