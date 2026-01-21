Odd = lambda No : (No % 2 == 1)

def main():
    Data = [41,44,43,67,98,40]
    print("Actual Data is :",Data)
    
    fData = list(filter(Odd,Data))
    print("Data after filter is :",fData)
if __name__  == "__main__":
    main()