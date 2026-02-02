
import sys

def main():
    if(len(sys.argv) == 3):

        file1 = sys.argv[1]
        fobj1 = open(file1,"r")
        Data1 = fobj1.read()
        
        file2 = sys.argv[2]
        fobj2 = open(file2,"r")
        Data2 = fobj2.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")
    else:
        print("There is no all Data")
        

if __name__ == "__main__":
    main()