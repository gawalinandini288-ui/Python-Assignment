from functools import reduce

Greater_70 = lambda No : No >= 70
Increment = lambda No : No + 10
Product_All = lambda A,B : A*B

def main():
    Data = [4,34,36,76,68,24,89,23,86,90,45,70]
    print("Actual Data is :",Data)

    fData = list(filter(Greater_70,Data))
    print("Data after filter :",fData)

    mData = list(map(Increment,fData))
    print("Data after map is :",mData)

    rData = reduce(Product_All,mData)
    print("Data after reduce is :",rData)

if __name__ =="__main__":
    main()