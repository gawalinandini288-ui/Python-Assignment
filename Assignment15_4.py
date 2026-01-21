from functools import reduce

Addition = lambda No1,No2 : No1 + No2

def main():
    Data = [43,67]
    print("Actual Data is :",Data)

    rData = reduce(Addition,Data)
    print("Data after reduce :",rData)
if __name__ == "__main__":
    main()