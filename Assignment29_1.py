import os 

def main():

    FileName = input("Enter the file name :")
    Ret = os.path.exists(FileName)

    if(Ret == True):
        open(FileName,"r")
        print("File gets opened successfully")
    else:
        print("There is no such a directory")



if __name__ == "__main__":
    main()