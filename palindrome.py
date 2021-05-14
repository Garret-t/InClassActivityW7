def palindrome(input):
    if input == "".join(reversed(input)):
        return True
    return False

if __name__ == "__main__":
    user_in = input('Enter a string: ')
    print(palindrome(user_in))