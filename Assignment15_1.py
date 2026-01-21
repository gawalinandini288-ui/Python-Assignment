
Square = lambda No : (No**2)

def main():
    Data = [11,12,13,14,15]
    print("Actual Data is :",Data)
    
    mData = list(map(Square,Data))
    print("Data after map is :",mData)
if __name__  == "__main__":
    main()