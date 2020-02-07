# Requirement:
# Write a program that prints ther first n triangular numbers.

# Implemented on Python 3.

print('This program will print the first n triangular numbers.')

n = int(input('Enter n: '))

for i in range(1, n + 1):
    print((i * (i + 1)) // 2)
