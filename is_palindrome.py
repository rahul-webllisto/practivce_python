
def is_palindrome(word):
    if word == word[::-1]:
        print("is a palindrome")        
    else:
        print("not a palindrome")



if __name__ == '__main__':
    word = input("enter a word: ").strip().lower()
    is_palindrome(word)
