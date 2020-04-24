"""
1.python函数参数这块看的不是很明白，默认值只会执行一次，这条规则在默认值为可变对象时很重要，希望老师再举个例子讲解一下；
2.函数的缩进特别关键，如果格式不对，就会返回语法错误，如何确保缩进格式的正确书写？
3.print和return的区别以及应用场景
4.字典传参和元组传参，解包参数列表这
5.字面量插值这块求实例
"""


class Name:
    age = 111
    def __init__(self):
        self.name = "bob"
    def name_n(self):
        self.joey = 111
        return self.name


print(Name.age)
