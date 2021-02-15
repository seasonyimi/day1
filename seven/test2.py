class Student():
    name='七月'
    age=0
    def __innit__(self,name,age):
        # 实例变量
        # 初始化对象的属性
        self.name=name
        self.age=age

student1=Student('石敢当',17)
print(student1.name)