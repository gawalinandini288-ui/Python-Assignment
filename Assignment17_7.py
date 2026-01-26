def Numbers(n):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            print(j,end = " ")
def main():
    n = int(input("Enter thr number :"))
    Numbers(n)
if __name__ == "__main__":
    main()
    