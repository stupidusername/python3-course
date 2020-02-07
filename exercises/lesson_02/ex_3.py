# Requirement:
# Write a program that given two numbers m and n prints a list of the natural
# numbers up to m * n that are not divisible by 3.

# Implemented on Python 3.

m = int(input('Enter m: '))
n = int(input('Enter n: '))

print([i for i in range(m * n + 1) if i % 3])
