# 李禄波
# 2021/2/16 10:26

# property属性：
# 把方法当作属性一样去使用
# 这个方法一定有返回值

class Person:
    def __init__(self, age=0):
        self.__age = age

    # 私有属性能够起到数据过滤的效果
    # def set_age(self, new_age):
    #     if 0 < new_age < 200:
    #         self.__age = new_age
    #     else:
    #         print("？？？？？")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if 0 < new_age < 200:
            self.__age = new_age
        else:
            print("你输入的年龄有误")


p = Person()
p.age = 12
print(p.age)