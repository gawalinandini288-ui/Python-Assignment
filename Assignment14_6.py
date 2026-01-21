CheckEvenOdd = lambda No : (No % 2 == 0)
No = int(input("Enter the number :"))

def main():
    if(No % 2 == 1):
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()