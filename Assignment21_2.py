import threading

def Maximum(Num):
    
    Max_Num = Num[0]
    for No in Num:
        if No > Max_Num:
            Max_Num = No
    print("Maximum Number :",Max_Num)


def Minimum(Num):
    
    Mini_Num = Num[0]
    for No in Num:
        if No <  Mini_Num:
            Mini_Num =  No
    print("Minimum Number :",Mini_Num)



def main():
    No = int(input("Enter the number of elements :"))
    Value = 0
    Num = list()

    print("Enter the numbers :")

    for i in range(No):
        Value = int(input())
        Num.append(Value)
    print("Actual Data is :",Num)

    MaxNum = threading.Thread(target=Maximum,args=(Num,))
    MiniNum = threading.Thread(target=Minimum,args=(Num,))

    MaxNum.start()
    MiniNum.start()

    MaxNum.join()
    MiniNum.join()

if __name__ == "__main__":
    main()

