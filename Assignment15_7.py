Strings = lambda Strs : len(Strs) > 5

def main():
    Data = ["Pune","Mumbai","Solapur","Nashik","Latur"]
    print("Actual Data is :",Data)

    fData = list(filter(Strings,Data))
    print("Data after filter is :",fData)

if __name__ == "__main__":
    main()