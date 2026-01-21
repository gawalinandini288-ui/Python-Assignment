def Addition(No1, No2):
    Ans = 0
    Ans = No1 + No2
    print("Addition of two Numbers :",Ans)

def Substraction(No1,No2):
    Ans = 0
    Ans = No1 - No2
    print("Substarction of two Numbers :",Ans)

def Multiplication(No1,No2):
    Ans = 0
    Ans = No1 * No2
    print("Multiplication of two numbers :",Ans)

def Division(No1,No2):
    Ans = 0
    Ans = No1 / No2
    print("Division of two numbers :",Ans)

def main():
    No1 = int(input("Enter the number :"))
    No2 = int(input("Enter the number :"))
    
    Addition(No1,No2)
    Substraction(No1,No2)
    Multiplication(No1,No2)
    Division(No1,No2)

if __name__ == "__main__":
    main()