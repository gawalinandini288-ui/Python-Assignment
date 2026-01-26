def Add(No1,No2):
    Ans = 0
    Ans = No1 + No2 
    print("Addition of these two numbers :",Ans)

def main():
    No1 = int(input("Enter the first number :"))
    No2 = int(input("Enter the second number :"))
    Add(No1,No2)
if __name__ == "__main__":
    main()