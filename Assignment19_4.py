from functools import reduce

Even_No = lambda No : No % 2 == 0
Sqaure_No = lambda No : No ** 2
Addition_All = lambda A,B : A + B

def main():
    Data = [5,2,3,4,3,4,1,2,8,10]
    print("Actual Data is :",Data)

    fData = list(filter(Even_No,Data))
    print("Data after filter is:",fData)

    mData = list(map(Sqaure_No,fData))
    print("Data after map is :",mData)

    rData = reduce(Addition_All,mData)
    print("Data after map is :",rData)

if __name__ == "__main__":
    main()