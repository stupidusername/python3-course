# Requirement:
# A library wants to store information about its books. Each book is identified
# by an ID number and has the following information related to it: title,
# author, year and number of copies. It is assumed that the ID used to find a
# book was always loaded beforehand.

# Implemented on Python 3.

books = {}  # dict used to store the books data.

while True:
    # Print menu options.
    print('-' * 20)
    print('Options:')
    print('a) Add a book.')
    print('f) Find a book.')
    print('e) Exit.')
    print()

    # Option input.
    option = input('Select an option: ')
    print()

    # Check the selected option.
    if option == 'a':
        # Add a book.
        id = int(input('ID: '))
        title = input('Title: ')
        author = input('Author: ')
        year = int(input('Year: '))
        copies = input('Number of copies: ')
        print()

        # Add the data to the books dict.
        books[id] = {
            'title': title,
            'author': author,
            'year': year,
            'copies': copies
        }

    elif option == 'f':
        # Find a book.
        id = int(input('ID: '))
        print('Title: ' + books[id]['title'])
        print('Author: ' + books[id]['author'])
        print('Year: ' + str(books[id]['year']))
        print('Number of copies: ' + str(books[id]['copies']))
        print()

    elif option == 'e':
        # Exit program.
        break

    else:
        # The selected option could not be recognized.
        print('The selected option is not valid.')
        print()
