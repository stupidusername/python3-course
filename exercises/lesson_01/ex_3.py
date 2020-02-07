# Requirement:
# Write a program that counts the number of even digits in n.

# Implemented on Python 3.

print('This program will count the number of even digits in n.')

n = int(input('Enter n: '))

even_q = 0
tmp = n

while True:
    digit = tmp % 10
    if not digit % 2:
        even_q += 1
    tmp //= 10
    if not tmp:
        break

print('There are ' + str(even_q) + ' even digits in ' + str(n) + '.')
