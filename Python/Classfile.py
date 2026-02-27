class pythonclass:
    class_name="This is my first class"


    def my_func(self):
        return "This is a test case"
    
py= pythonclass()
print(py.class_name)
print(py.my_func())

class mycontsructor:
     
    __my_private_variable="This is a Private variable" 
    

    global my_globalvariable
    my_globalvariable="This is a global variable"

    def __init__(self,name:str):
        self.name=name
        print("This is a constructor method")

    def get_name(self):
        return f"This is the name of this function {self.name}"
    
    
    def my_privatevariable(self):
        return f"{self.__my_private_variable}"
        

    
this_class=mycontsructor("waseem")
print(this_class.get_name())
print(this_class.my_privatevariable())
print(my_globalvariable)
    

       
