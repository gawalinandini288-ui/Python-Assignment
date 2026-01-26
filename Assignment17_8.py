def FactorialSum(No):
    Sum = 0
    for i in range(1,No+1):
        if No % i == 0:
            Sum += i
    return Sum
    print("FactorialSum is :",Sum)

def main():
    No = int(input("Enter the number :"))
    FactorialSum(No)
    
if __name__ == "__main__":
    main()