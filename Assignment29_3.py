
import sys

def main():
    if(len(sys.argv)==2):
        
        FName1 = sys.argv[1]
        fobj = open(FName1,"r")
        Data = fobj.read()
        print(Data)
    
        FName2 = input("Enter the new file name :")
        fobj1 = open(FName2,"w")
        Data1 = fobj1.write()
        print(Data1)
    
    else:
        print("There is no all data")
if __name__ == "__main__":
    main() 