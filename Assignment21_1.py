import threading

def Prime_No(Data):
    print("Prime Numbers :")
    for i in Data:
        if(i <= 1):
            continue
        is_prime = True
        for j in range(2,i):
            if (i % j == 0):
                is_prime = False
        if is_prime:
            print(i,end = " ")
    print()
   
def Not_PrimeNo(Data):
    print("Not Prime Numbers :")
    for i in Data:
        if(i <= 1):
            continue
        is_prime = True
        for j in range(2,i):
            if (i % j == 0):
             print(i,end = " ")
             break
    print()

def main():
    No = int(input("Enter thee number of elements :"))
    Value = 0
    Data = list()

    print("Enter elements :")

    for i in range(No):
        Value = int(input())
        Data.append(Value)
    print("Actual list :",Data)

    PrimeNo = threading.Thread(target=Prime_No,args=(Data,))
    NotPrimeNo = threading.Thread(target=Not_PrimeNo,args=(Data,)) 

    PrimeNo.start()
    NotPrimeNo.start()
 
    PrimeNo.join()
    NotPrimeNo.join()

if __name__ == "__main__":
    main()

        