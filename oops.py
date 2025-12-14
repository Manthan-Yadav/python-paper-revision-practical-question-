# # class and object
# class student:
#     def show(self):
#         print("this is a class")

# odj=student()
# odj.show()

# # method and attribute
# class car:
#     def brand(self,brand):
#         self.brand=brand
#     def drive(self):
#         print(self.brand,"car is driving")

# car1=car()
# car1.brand("bmw")
# car1.drive()

# # access specifier
# class user:
#     def __init__(self):
#         self.name="piblic"
#         self._email="protected"
#         self.__password="private"

# u=user()
# print(u.name)
# print(u._email)
# print(u.__password)

# # constructor
# class mobile:
#     def __init__(self,brand):
#         print("constructor is call")
#         self.brand=brand
# m1=mobile("samsung")

# # static method
# class math:
#     @staticmethod
#     def add(a,b):
#         return a+b
# print(math.add(10,20))

# # attribute
# class bank:
#     def __init__(self):
#         self.__balance=1000
#     def show_balance(self):
#         print(self.__balance)

# b=bank()
# b.show_balance()

# # encapsulation 
# class account:
#     def __init__(self):
#         self.__amount=0
#     def set_amount(self,amt):
#         self.__amount=amt
#     def get_amount(self):
#         return self.__amount
# a=account()
# a.set_amount(1000)
# print(a.get_amount())

# # inheritence
# class animal:
#     def sound(self):
#         print("animal sound")
# class dog(animal):
#     def bark(self):
#         print("dog bark")

# d=dog()
# d.sound()
# d.bark()

# # polymorphism
# class shape:
#     def area(self):
#         print("area of shape ")
# class square:
#     def area(self):
#         print("area of square")
# s=shape()
# sq=square()
# s.area()
# sq.area()