Largest = lambda No1,No2,No3 : ()

No1 = int(input("Enter the number :"))
No2 = int(input("Enter the number :"))
No3 = int(input("Enter the number :"))

def main():
    if (No1 > No2) and (No1 < No3):
        print("Largest number is :",No1)
    elif (No2 > No3):
        print("Largest number is :",No2)
    else:
        print("Largest number is:", No3)
if __name__ == "__main__":
    main()