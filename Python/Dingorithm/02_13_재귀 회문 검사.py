input = "abcba"

def is_palindrome(string):
    
    if len(string) <= 1:
        return True
    elif string[0] == string [-1]:
        return is_palindrome(string[1: -1])
    else: 
        return False

def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome(string[1:-1])
    
    
def is_palindrome(string):

    if string == string[::-1]:
        return True
    return False

print(is_palindrome(input))