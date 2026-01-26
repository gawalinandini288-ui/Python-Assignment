from functools import reduce

Double_No = lambda No : No * 2
Maximum_No = lambda A,B : A if A > B else B

def Prime_No(n):
    if n <= 1:
        return False
    for i in range(2,int(n **0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    Data = [2,70,11,10,17,23,31,77]
    print("Actuel Data is :",Data)

    fData = list(filter(Prime_No,Data))
    print("Data after filter is :",fData)

    mData = list(map(Double_No,fData))
    print("Data after map is :",mData)

    rData = reduce(Maximum_No,mData)
    print("Data after reduce is :",rData)

if __name__ == "__main__":
    main()