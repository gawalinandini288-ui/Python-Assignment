import os

def main():

    FileName = input("Enter the file name :")
    
    if(os.path.exists(FileName)):
        
        fobj = open(FileName,"r")
        Data = fobj.read()
        print(Data)
        
    else:
        print("There is no such directory")

if __name__ == "__main__":
    main()