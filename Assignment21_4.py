import threading
SumNo = 0
ProductNo = 1
lobj = threading.Lock()

def Sum(Data):
    global Sum_All
    SumNo = Sum(Data)
    with lobj:
        print("Addition is :")

def Product(Data):
    global Product_All
    ProductNo = Product(Data)
    with lobj:
        print("Multiplication is :")

def main():
    global SumNo , ProductNo
    No = int(input("Enter the number of elements :"))
    Value = 0
    Data = list()
    print("Enter the numbers :")

    for i in range(No):
        Value = int(input())
        Data.append(Data)
    print("Actual Data :",Data)

    SumAll = threading.Thread(target=Sum,args=(Data,))
    ProductAll = threading.Thread(target=Product,args=(Data))

    SumAll.start()
    ProductAll.start()

    SumAll.join()
    ProductAll.join()

if __name__ == "__main__":
    main()

