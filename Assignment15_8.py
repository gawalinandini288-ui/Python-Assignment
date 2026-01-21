Divisible = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Data = [15,21,15,45,90]
    print("Actual Data is :",Data)

    fData = list(filter(Divisible,Data))
    print("Data after filter is :",fData)
if __name__ == "__main__":
    main()