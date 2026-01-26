def ChkPrime(No):
    for i in range(2,No):
       if (No <= 1):
        print("It is Prime Number")
       else:
        print("It is not Prime Number")
def main():
    Value = int(input("Enter the number :"))
    ChkPrime(Value)
if __name__ == "__main__":
    main()