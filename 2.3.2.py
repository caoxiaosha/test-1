# python3.6版本
# f字符串,f是format(设置格式)的简写,
first_name = "河"
last_name = "小象"
full_name = f"{first_name}{last_name}"
print(full_name)

# f字符串的使用方法
print(f"Hello {full_name.title()}")

# 使用f字符串创建消息,再将消息赋值给变量
first_name = "he"
last_name = "xiaoxiang"
full_name = f"{first_name}{last_name}"
message = f"Hello {full_name.upper()}"
print(message)

# python3.6之前版本
first_name = "he"
last_name = "xiaoxiang"
full_name = "{}{}".format(first_name,last_name)
print(full_name)
full_name = "Hello {}{}".format(first_name,last_name)
print(full_name)
full_name = "Hello {}{}".format(first_name.title(),last_name.title())
print(full_name)



