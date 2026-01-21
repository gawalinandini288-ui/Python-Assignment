def Palindrome(No):
    First = No 
    Result = 0

    while No > 0 :
        Num = No % 10
        Result = Result * 10 + Num
        No = No // 10
    if First == Result:
        print("It is Palindrome Number")
    else:
        print("It is not Palindrome Number")
def main():
    No = int(input("Enter the Number :"))
    Palindrome(No)
if __name__ == "__main__":
    main()