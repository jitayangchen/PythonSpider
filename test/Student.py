class People(object):
    def say_hi(self):
        print 'Hello lalala'


class Student(People):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        super(Student, self).say_hi()
        print 'Hahaha'

    def exception(self):
        try:
            print 'try...'
            r = 1 / 0
            print 'result: ', r
        except BaseException, e:
            print 'except: ', e
        finally:
            print 'finally...'
        print 'END'


p = Student('YYY')
# p.exception()
p.say_hi()
