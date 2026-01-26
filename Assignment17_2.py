def Star(n):
    for i in range(n):
        print("  *  "*n)
def main():
    No = int(input("Enter the Number :"))
    Star(No)
if __name__ == "__main__":
    main()