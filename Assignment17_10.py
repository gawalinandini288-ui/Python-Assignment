def Sum_Digit(n):
    Result = 0 
    No = str(n)
    Result = Result + str(n)
    print("Sum of Digits :",Result)
def main():
    No = int(input("Enter the number"))
    Sum_Digit(No)
if __name__ == "__main__":
    main()
