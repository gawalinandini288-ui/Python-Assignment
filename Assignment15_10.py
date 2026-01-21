

def main():
    Data = [11,12,14,19,20,22]
    print("Actual Data is :",Data)

    fData = len(list(filter(lambda No : No % 2 == 0 ,Data)))
    print("Data after filter is :",fData)

if __name__ == "__main__":
    main()