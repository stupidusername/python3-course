# Requirement:
# Check if a word is a palindrome.

# Implemented on Python 3.6.

word = input('Enter a word: ')

palindrome = word.lower() == word[::-1].lower()

if palindrome:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
