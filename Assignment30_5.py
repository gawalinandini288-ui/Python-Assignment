def main():

        
        File1 = input("Enter the file name :")
        fobj1 = open(File1,"r")
        Data = fobj1.read()

        Word = input("Enter the word :")
        count = Data.count(Word)
        
        if(count >= 1):
              print("Yes")
        else:
              print("No")

if __name__ == "__main__":
    main()