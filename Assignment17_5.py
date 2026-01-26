def Star(n):
    for i in range(n):
       print("  *  " * (n-i))
       
def main():
    n = int(input("Enter the number :"))
    Star(n)
if __name__ == "__main__":
    main()