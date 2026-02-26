# global my_globalvariable #it can be accessed even if we define it outside the class
# my_globalvariable="This is global variable defined outside the class"
    
# class my_encapsulation:

#     __my_private_variable="This is a private variable" #Once you define the private variable it can only be called once defined in the method

#     _my_protected_variable="This is a protected variable" #we can define it within the class and can be called without creating a method

#     def __init__(self,name:str):
#         self.name=name
#         print("This is a constructor method")


#     def get_name(self):
#         return f"This is my first function with name {self.name}"
    
#     def get_private_variable(self):
#         return f"{self.__my_private_variable}"

    

# encap=my_encapsulation("waseem")
# print(my_globalvariable)
# print(encap._my_protected_variable)
# print(encap.get_private_variable())
# print(encap.get_name())

#This is Multiple Inheritance which has two parent class and one child class and we can inherit both parent classes in child class
# class Parent_inheritane:


#     def my_add(self,x,y):
#         self.x=x
#         self.y=y
#         return f"This is addition {self.x + self.y}"

# class multi_parent_class:

#  def credentials(self,username:str,password:str):
#     self.username=username
#     self.password=password
#     return f"This has username and password {self.username.upper().split(),self.password.upper().split()}"
    

    
# class child_inheritance(Parent_inheritane,multi_parent_class):

#     def my_multiplication(self):
#         return f"This is multiplication {self.x * self.y}"
    

# p=child_inheritance()
# print(p.my_add(5,6))
# print(p.my_multiplication())
# print(p.credentials("Username","Password"))

#Multilvel inheritance is where one is inherited from the other like as below child 1 is inherited from parent class and child 2 is inherited from
#child 1 class its like chain of inheritance
# class car:
#     def get_car(self):
#         return "This is Hyundai"
    
# class child1_car(car):
#     def get_car1(self):
#         return "This is maruti"
    
# class child2_car(child1_car):
#     def get_car2(self):
#         return "This is kia"
    
# child2=child2_car()
# print(child2.get_car())
# print(child2.get_car1())
# print(child2.get_car2())


#hierarchial Inheritance is where it will have multiple child classes with one parent class

# class A:

#     def show(self):
#         return "This is a show"
# class B(A):
#     def show1(self):
#         pass
# class C(A):
#     def show2(self):
#         pass

# my_class=C()
# b=B()
# print(my_class.show())
# print(my_class.show2())
# print(b.show1())

# class bank_account:

#     total_deposits=0 #class level tracking
    
#     def __init__(self,name:str,balance):
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount
#         bank_account.total_deposits+=amount
#         return f"{self.name} now has balance {self.balance}"
#     @classmethod
#     def no_of_deposits(cls):
#         return f"Total deposits is equal to {cls.total_deposits}"

# acc1=bank_account("waseem",5000)
# acc2=bank_account("nadeem",6000)
# print(acc1.deposit(1000))
# print(acc2.deposit(2000))
# print(bank_account.no_of_deposits())
# from abc import ABC,abstractmethod
# class vehicle(ABC):

#     @abstractmethod
#     def start(self):
#         print("Vehicle is started")
    
#     @abstractmethod
#     def stop(self):
#         print ("Vehicle is stopped")



# class car(vehicle):
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False

#     def start(self):
#         self.acc=True
#         self.brk=True
#         self.clutch=True
#         print("Car is started")
    
#     def stop(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#         print("Car is stopped")

# c=car()
# c.start()
# c.stop()
#File Input output
    
# f=open("practice.py","r")
# data=f.readline()
# print(data)
# print(type(data))
# f.close()

# with open("practice.py", "r") as f:
#     text = f.read()

# words = text.split()
# print("Total words:", len(words))

#property

# class my_property:

#     def __init__(self,phy,chem,maths):
#         self.phy=phy
#         self.chem=chem
#         self.maths=maths
#         self.totalmarks=str(round((self.phy+self.chem+self.maths)/3)) + "%"

#     @property
#     def calculation(self):
#       return str(round((self.phy+self.chem+self.maths)/3)) + "%"


# class1=my_property(98,85,85)
# print(class1.calculation)
# class1.chem=100
# print(class1.calculation)

# class private_class:

#     def __init__(self,marks):
#         self.__marks=marks

#     def get_marks(self):
#         return self.__marks
    
#     def set_marks(self,value):
#         if value>0 and value<=100:
#             self.__marks=value
#         else:
#             print("Invalid marks")



# private =private_class(50)
# print(private.get_marks())
# private.set_marks(95)
# print(private.get_marks())

class Bird:
    def fly(self):
        print("Bird is flying")
    
class Airplane(Bird):
    def fly(self):
        super().fly()
        print("Aiplane is flying")

a=Bird()
b=Airplane()
a.fly()
b.fly()

