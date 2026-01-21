from functools import reduce

Product = lambda A,B : A*B

def main():
    Data = [11,12,13,14,15]
    print("Actual Data is :",Data)

    rData = reduce(Product,Data)
    print("Data after reduce : ",rData)
if __name__ == "__main__":
    main()