def Prime(No):
    for i in range(2,No):
        if (No <= 1):
            print("It is not prime number")
        else:
            print("It is prime number")
def main():
    No = int(input("Enter thr number:"))
    Prime(No)
if __name__ == "__main__":
    main()
