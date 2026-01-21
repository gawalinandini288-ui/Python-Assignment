def Even(No):
    for i in range(2,  No + 1,2):
        print(i,end=" ")
def main():
    No = int(input("Enter the number :"))
    Even(No) 
if __name__ == "__main__":
    main()