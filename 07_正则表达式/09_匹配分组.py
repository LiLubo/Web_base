# 李禄波
# 2021/2/16 13:11

import re

# |	匹配左右任意一个表达式
# (ab)	将括号中字符作为一个分组
# data = 're_d@qq.com'
#
# try:
#     ret = re.match("([a-z|A-Z|0-9|_]+)@(163|aliyun|qq)\.(com|cn)", data)
#     # ret.group()不带参数则获取所有的数据
#     info = ret.group()
#     # ret.group(i)获取第i个组的数据
#     # ret.group(1)....
# except Exception as e:
#     print(e)
# else:
#     print(info)

# \num	引用分组num匹配到的字符串
# data = '<div>nihao</div>'
#
# try:
#     ret = re.match('<[a-zA-Z0-9]{1,20}>.*</[a-zA-Z0-9]{1,20}>', data)
#     # ret.group()不带参数则获取所有的数据
#     info = ret.group()
#     # ret.group(i)获取第i个组的数据
#     # ret.group(1)....
# except Exception as e:
#     print(e)
# else:
#     print(info)

# data = '<html><div>nihao</div></html>'
#
# try:
#     ret = re.match('<([a-zA-Z0-9]{1,20})><([a-zA-Z0-9]{1,20})>.*</\\2></\\1>', data)
#     # ret.group()不带参数则获取所有的数据
#     info = ret.group()
#     # ret.group(i)获取第i个组的数据
#     # ret.group(1)....
# except Exception as e:
#     print(e)
# else:
#     print(info)

# (?P<name>)	分组起别名
# (?P=name)	引用别名为name分组匹配到的字符串
data = '<html><div>nihao</div></html>'

try:
    ret = re.match('<(?P<name1>[a-zA-Z0-9]{1,20})><(?P<name2>[a-zA-Z0-9]{1,20})>.*</(?P=name2)></(?P=name1)>', data)
    # ret.group()不带参数则获取所有的数据
    info = ret.group()
    # ret.group(i)获取第i个组的数据
    # ret.group(1)....
except Exception as e:
    print(e)
else:
    print(info)

