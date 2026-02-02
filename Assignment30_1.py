import os

def main():
    Count = 0
    FileName = input("Enter the file name :")

    if(os.path.exists(FileName)):

        fobj = open(FileName,"r")
        Data = fobj.read()

        for line in fobj:
            Count = Count + 1
        print("Total number of lines in given file :",Count)
    
    else:
        print("Nothing")
if __name__ == "__main__":
    main()
