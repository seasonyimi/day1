class Homework():
    object='语文'
    sum=3
    teacher='张老师'
    def do_homework(self):
        print('这是'+self.object+'作业')
        print('一共'+str(self.sum)+'样')
        print('任课老师是'+self.teacher)
    
    def __init__(self):
        #构造函数
        print('student')

student_homework=Homework()
student_homework.do_homework()
student_homework.__init__()
