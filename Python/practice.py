"""def cal_age(age):
 if age<=0:
    raise ValueError("Age cannot be zero")
 return 10/age
print(cal_age(0))
"""

"""class my_point:
   def __init__(self,x,y):
    self.x=x
    self.y=y

   @classmethod
   def zero(cls):
    return cls(5,5)


   def my_draw(self):
    print(f"{self.x+self.y}")
    return "This is addition"

my_class =my_point(0,0)
my_class=my_point.zero()
print(my_class.my_draw())"""


"""class second_class:

    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __str__(self):
       return f"({self.x},{self.y})"
        


    def draw(self): 
        print(f"{self.x * self.y}")
        return "This is multiplication"
    
    def string_letter(self):
        print(f"({self.x},{self.y})")
        return "This is string"


num_obj=second_class(8,8)
print(num_obj.draw())
str_obj=second_class("x","y")
print(str_obj.string_letter())

print(str(str_obj))"""


"""class third_class:


    def __init__(self,x,y):
        self.x=x
        self.y=y

    
    def __add__(self,other):
        return third_class(self.x + other.x,self.y + other.y)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    

class_1=third_class(30,40)
class_2=third_class(10,20)
print(class_1 + class_2)"""

"""class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")     
        self.__price = value

    price = property(get_price, set_price)


# Correct usage
try:
    p = Product(-50)
except ValueError as e:
    print(e)   # Output: Price cannot be negative

p = Product(100)
print(p.price)  # Output: 100

p.price = 200
print(p.price)  # Output: 200
"""



        













