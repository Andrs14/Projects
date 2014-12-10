def is_palindrome(str):
    reverse = str[::-1]
    if str == reverse:
        print(str + ' is a palindrome')
    else:
        print(str + ' is not a palindrome')

def main():
    import sys
    is_palindrome((sys.argv[1]))

if __name__ == '__main__':
    main()
    
