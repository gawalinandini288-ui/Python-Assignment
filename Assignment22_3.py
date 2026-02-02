class Arithematic:
      
    Value1 = 0
    Value2 = 0

    
    def __init__(self):

        self.Value1 = 0
        self.Value2 = 0
    
    def Accept(self):
        self.Value1 = int(input("Enter the first number :"))
        self.Value2 = int(input("Enter the second number :"))
    
    def Addition(self):
        Add =  self.Value1 + self.Value2
        print("Addition is :",Add)
     
    def Substraction(self):
        Sub =   self.Value1 - self.Value2 
        print("Substraction is",Sub)
     
    def Multiplication(self):
        Mult =  self.Value1 * self.Value2 
        print("Multiplication is :",Mult) 
     
    def Division(self):
        try:
           Div =  self.Value1 / self.Value2 
           print("Division is :",Div)
        except ZeroDivisionError:
            print("Cannot Divisible By Zero")
    

obj1 = Arithematic()
obj2 = Arithematic()
obj3 = Arithematic()
 
obj1.Accept()
obj1.Addition()
obj1.Substraction()
obj1.Multiplication()
obj1.Division()
 
print("\n")
    
obj2.Accept()
obj2.Addition()
obj2.Substraction()
obj2.Multiplication()
obj2.Division()
    
print("\n")
    
obj3.Accept()    
obj3.Addition()
obj3.Substraction()
obj3.Multiplication()
obj3.Division()
    