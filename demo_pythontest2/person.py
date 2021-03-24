class Person:
    # pass 无意义，定义一个空的类（占位）

    # 静态属性
    name = None
    gender = "male"
    age = 0

    # 私有属性
    # 私有属性不能通过对象直接访问，可以通过方法进行访问
    __money = 1000

    # 动态方法
    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print("sleeping")

    def run(self):
        print("running")

    # 这是一个构造方法，当实例化对象的时候会先去调用这个方法
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def have_money(self):
        return self. __money

    # 私有方法，不能通过对象直接访问
    def __get_money(self):
        return self.__money+1000


# 类的实例化

# name,gender,age不写时需按照参数传入定义顺序赋值，写之后可以打乱顺序
p1 = Person(name="zhangsan", gender="female", age=20)
print(p1.name)
p1.eat()

p2 = Person("lisi", "female", 30)
print(p2.name)
p2.eat()
print(p2.run())  # run()没有return，打印时打印None
print(p2.have_money())

p2.__get_money()
