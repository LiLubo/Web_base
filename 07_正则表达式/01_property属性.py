# 李禄波
# 2021/2/16 10:26

# property属性：
# 把方法当作属性一样去使用
# 这个方法一定有返回值

class Person:
    def __init__(self, age):
        self.age = age

    @property   # get_age就变成了property属性
    def get_age(self):
        return self.age


# 没有property属性的情况下
p = Person(100)
# ret = p.get_age()
# print(ret)

# 有property属性的情况下
print(p.get_age)