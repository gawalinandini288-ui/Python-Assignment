def Minimum(Data):
    Min_Num = Data[0]
    for No in Data:
        if No < Min_Num:
            Min_Num = No
    return Min_Num

def main(): 
    Size = 0
    Value = 0
    Ret = 0

    print("Enter thr number of elements :")
    Size = int(input())

    Data = list()

    print("Enter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    Ret = Minimum(Data)
    
    print("Minimum Number is :",Ret)

if __name__ == "__main__":
    main()