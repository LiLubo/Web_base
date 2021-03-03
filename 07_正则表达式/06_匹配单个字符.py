# 李禄波
# 2021/2/16 12:29

# .	    匹配任意1个字符（除了\n）
# [ ]	匹配[ ]中列举的字符
# \d	匹配数字，即0-9
# \D	匹配非数字，即不是数字
# \s	匹配空白，即 空格，tab键
# \S	匹配非空白
# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# \W	匹配特殊字符，即非字母、非数字、非汉字

import re

# .	    匹配任意1个字符（除了\n）
# ret = re.match("t.o", "tqo")
# info = ret.group()
# print(info)

# [ ]	匹配[ ]中列举的字符
# try:
#     ret = re.match("t[abc]o", 'tpo')
#     info = ret.group()
# except Exception as e:
#     print("匹配失败", e)
# else:
#     print(info)

# \d	匹配数字，即0-9
# try:
#     ret = re.match("t\do", 't9o')
#     info = ret.group()
# except Exception as e:
#     print("匹配失败", e)
# else:
#     print(info)

# \D	匹配非数字，即不是数字
# try:
#     ret = re.match("t\Do", 't1o')
#     info = ret.group()
# except Exception as e:
#     print("匹配失败", e)
# else:
#     print(info)

# \s	匹配空白，即 空格，tab键
# try:
#     ret = re.match("t\so", 't\to')
#     info = ret.group()
# except Exception as e:
#     print("匹配失败", e)
# else:
#     print(info)

# \S	匹配非空白
# try:
#     ret = re.match("t\So", 't o')
#     info = ret.group()
# except Exception as e:
#     print("匹配失败", e)
# else:
#     print(info)

# \w	匹配非特殊字符，即a-z、A-Z、0-9、_、汉字
# try:
#     ret = re.match("t\wo", 't@o')
#     info = ret.group()
# except Exception as e:
#     print("匹配失败", e)
# else:
#     print(info)

# \W	匹配特殊字符，即非字母、非数字、非汉字
# try:
#     ret = re.match("t\Wo", 'to')
#     info = ret.group()
# except Exception as e:
#     print("匹配失败", e)
# else:
#     print(info)