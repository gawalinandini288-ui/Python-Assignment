import os

def main():
    FName1 = input("Enter the existing file :")
    if(os.path.exists(FName1)):
        fobj = open(FName1,"r")
        Data = fobj.read()
        print(Data)
    else:
        print("There is no such directory")
    
    FName2 = input("Enter the new file name :")
    fobj1 = open(FName2,"w")
    Data1 = fobj1.write()
    print(Data1)
    

if __name__ == "__main__":
    main() 