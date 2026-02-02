def main():
    Count = 0
    FileName = input("Enter the file name :")

    fobj = open(FileName,"r")
    
    for line in fobj:
        Words = line.split()  
        Count = Count + len(Words)
    print("Number of words in file :",Count)

if __name__ == "__main__":
    main()