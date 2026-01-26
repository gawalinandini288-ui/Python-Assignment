import threading

def Even():
    print("Even Thread :")
    for i in range(2,21,2):
        print(i,end = " ")

def Odd():
    print("Odd Thread :")
    for i in range(1,20,2):
        print(i,end =" ")

def main():
    Even()
    Odd()
        
EvenAll = threading.Thread(target = Even,args="Even")
OddAll = threading.Thread(target = Odd,args="Odd")
EvenAll.start()
OddAll.start()

EvenAll.join()
OddAll.join()

if __name__ == "__main__":
    main()


