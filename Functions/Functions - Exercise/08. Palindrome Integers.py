numbers = input().split(", ")

def palindrome_check(number):
    for i in number:
        if i == i[::-1]:
            print("True")
        else:
            print("False")


palindrome_check(numbers)

