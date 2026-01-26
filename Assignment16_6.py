def ChkNum(No):
    if (No > 0):
        print("It is positive number")
    elif (No < 0):
        print("It is negative number")
    else:
        print("It is zero")
def main():
    No = int(input("Enter thr number :"))
    ChkNum(No)
if __name__ == "__main__":
    main()