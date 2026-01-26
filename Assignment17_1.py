def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2
    print("Addition Of These Numbers :",Ans)

def Sub(No1,No2):
    Ans = 0
    Ans = No1 - No2
    print("Substraction Of These Numbers :",Ans)

def Mult(No1,No2):
    Ans = 0
    Ans = No1 * No2
    print("Multiplication Of These Numbers :",Ans)

def Div(No1,No2):
    Ans = 0
    Ans = No1 / No2
    print("Division Of These Numbers :",Ans)

def main():
    
    No1 = int(input("Enter the number :"))
    No2 = int(input("Enter the number :"))

    Add(No1,No2)
    Sub(No1,No2)
    Mult(No1,No2)
    Div(No1,No2)
if __name__ == "__main__":
    main()