def palindrome():
    num=input("Enter the value to be checked:- ")
    if num==num[::-1]:
        print(f"{num} is palindrome")
    else:
        print(f"{num} is not palindrome")

palindrome()
