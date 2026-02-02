class Demo:

    def __init__(self,No1,No2):
        self.Value1 = No1
        self.Value2 = No2

    def Fun(self,No1,No2):
        No1 = int(input())
        No2 = int(input())
    
    def Gun(self,No1,No2):
        No1 = int(input())
        No2 = int(input())


obj1 = Demo(11,21)
obj2 = Demo(51,101)

print("Instance Variable of obj1 :",obj1.Value1,obj1.Value2)
print("Instance Variable of obj1 :",obj2.Value1,obj2.Value2)

