# Requirement:
# Given a text extract the following information:
#   - The number of total words.
#   - The longest word and its number of letters.
#   - The number of times each word appears.

# Implemented on Python 3.6.

text = input('Enter a text: ')

# Build a list that contains each word converted to lower case.
words = text.lower().split()

# Remove chars that should not be part of words.
words = [word.strip('¡!¿?\'".:,(){}[];<>') for word in words]

# Remove empty strings.
words = [word for word in words if word]

# Build a set of unique words.
unique_words = set(words)

# Count the number of times that each word appears.
word_count = {word: words.count(word) for word in unique_words}

# Find the longest word.
longest = None
for word in unique_words:
    if not longest or len(word) > len(longest):
        longest = word

# Print output.
print('-' * 15)
if len(words):
    print(f'Number of words: {len(words)}')
    print(f'Longest word: {longest} ({len(longest)})')
    print(f'Word count:')
    for word, count in word_count.items():
        print(f'\t{word}: {count}')
else:
    print('The given text does not contain any word.')
