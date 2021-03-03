# 李禄波
# 2021/2/16 10:26

# property属性：
# 把方法当作属性一样去使用
# 这个方法一定有返回值

class Person:
    def __init__(self, age=0):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        self.__age = new_age

    # age 就是 property属性
    # 参数1：获取property属性的方法
    # 参数2：设置property属性的方法
    age = property(get_age, set_age)


p = Person()
p.age = 12
print(p.age)