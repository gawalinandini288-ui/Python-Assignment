Minimum = lambda No1,No2 : (No1 > No2)
No1 = int(input("Enter the first number :"))
No2 = int(input("Enter the second number :"))


def main():
    print("Minimum is number :")
    if(No1 < No2):
        print(No1)
    else:
        print(No2)
    
if __name__ == "__main__":
    main()