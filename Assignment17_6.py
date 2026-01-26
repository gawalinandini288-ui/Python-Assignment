def Numbers(n):
    for i in range(n):
        for i in range(1,n + 1,1):
            print(i,end = " ")
    
def main():
    n = int(input("Enter the number :"))
    Numbers(n)
    
if __name__ == "__main__":
    main()