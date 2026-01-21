Divisible = lambda No : (No % 5 == 0)
No = int(input("Enter the number :"))

def main():
    if(No % 5 == 0):
        print("True")
    else:
        print("False")
if __name__ == "__main__":
    main()