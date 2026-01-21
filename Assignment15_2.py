Even = lambda No : (No % 2 == 0)

def main():
    Data = [22,23,26,27,28,29,20]
    print("Actual Data is :",Data)
    
    fData = list(filter(Even,Data))
    print("Data after filter is :",fData)
if __name__  == "__main__":
    main()