# 李禄波
# 2021/2/16 12:57

import re
# ^	匹配字符串开头
data = '2Aafg@itcast.cn'

try:
    ret = re.match("^\d[a-zA-Z0-9_]{4,10}@itcast\.cn", data)
    info = ret.group()
except Exception as e:
    print(e)
else:
    print(info)

# $	匹配字符串结尾
data = '2Aafa@itcast.cn'

try:
    ret = re.match("[a-zA-Z0-9_]{4,10}@itcast\.c[n]$", data)
    info = ret.group()
except Exception as e:
    print(e)
else:
    print(info)