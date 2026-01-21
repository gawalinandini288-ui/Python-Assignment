def ChkVowel(Alpha):
    if Alpha.lower() in ["a","e","i","o","u"]:
        print("It is Vowel")
    else:
        print("It is not Vowel")
def main():
    Alpha = input("Enter the letter :")
    ChkVowel(Alpha)
if __name__ == "__main__":
    main()