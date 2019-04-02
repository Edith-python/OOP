
# 定义一个学生类，用来形容学生
# 定义一个空类
class Student():
    # 一个空类，pass代表直接跳过
    # 此处pass必须有
    pass

# 定义一个对象
Amy = Student()

# 定义一个类，用来描述听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1. def doHomework的缩进
    # 2. 系统默认一个self参数
    def doHomework(self):
        print("I'm doing.")

        # 推荐在函数末尾使用None
        return None

# 实例化一个学生Amy,是一个具体的人
Amy = PythonStudent()
print(Amy.name)
print(Amy.age)
# 注意成员函数的调用没有向内传递参数
Amy.doHomework()