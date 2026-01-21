def Sum_Digit(No):
    Result = 0
    for i in str(No):
        Result = Result + str(Sum_Digit)
    print("Sum of digits :",Result)
def main():
    No = int(input("Enter the Number: "))
    Sum_Digit(No)
if __name__ == "__main__":
    main()