def Binary(No):
    binary = " "
    while No > 0:
        binary = str(No % 2) + binary
        No = No // 2
    return binary
def main():
    No = int(input("Enter thr Number:"))
    Binary(No)
if __name__== "__main__":
    main()