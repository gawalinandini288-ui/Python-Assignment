import sys

def main():
    if(len(sys.argv)==3):

        Count = 0
        File1 = sys.argv[1]
        fobj1 = open(File1,"r")
        Data = fobj1.read()

        A = sys.argv[2]
        Count = Data.count(A)
        print("Frequnecy count of string :",Count)

    else:
        print("There is all Data")
if __name__ == "__main__":
    main()
