# class A(object):
#     pass
#
# print A.__name__
# print A.__dict__
# print A.__module__
# print A.__bases__
# a = A()
#
#
# class Cat:
#     __metaclass__ = type
#     def __init__(self):
#         self.hungry = True
#
#     def eat(self):
#         if self.hungry:
#             print 'I am hangry...'
#             self.hungry = False
#         else:
#             print 'No, thanks!'
#
#
# class Barsik(Cat):
#
#     def __init__(self):
#         super(Barsik, self).__init__()
#         self.sound = 'Aaaammm!'
#
#         print self.sound
#
#
# brs = Barsik()
# brs.eat()

# import sys
#
#
# class Limiter(object):
#     # __slots__ = ['age', 'name', 'job']
#     __slots__ = 'aaaa'
#
# class A(object):
#     age = ''
#     name = ''
#     job = ''
#
#
# print sys.getsizeof(Limiter)
# print sys.getsizeof(A)
# print '=' * 10
# print sys.getsizeof(Limiter())
# print sys.getsizeof(A())

BaseException
class Point:
  __slots__ = ()
  x = ExternalStorage("x")
  y = ExternalStorage("y")
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

a = Point()
a.__slots__
a.__dict__