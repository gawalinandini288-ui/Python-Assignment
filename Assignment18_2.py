def Maximum(Data):
    Max_Num = Data[0]
    for No in Data:
        if No > Max_Num:
            Max_Num = No
    return Max_Num

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
    
    Ret = Maximum(Data)
    
    print("Maximum Number is :",Ret)

if __name__ == "__main__":
    main()