import threading

def EvenFactor(Data):
    Sum =0
    EvenFactor = [i for i in range(2,Data + 1,2) if Data % i == 0]
    Sum_Even = Sum(EvenFactor)
    print("Even Factors :",EvenFactor)
    print("Sum of even factors :",Sum_Even)

def OddFactor(Data):
    Sum = 0
    OddFactor = [i for i in range(1,Data + 1,2) if Data % i == 0]
    Sum_Odd = Sum(OddFactor)
    print("Odd Factors :",OddFactor)
    print("Sum of odd factors :",Sum_Odd)

def main():
    Data = int(input("Enter the number :"))

    Even = threading.Thread(target = EvenFactor,args=(Data,))
    Odd = threading.Thread(target = OddFactor,args = (Data,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()