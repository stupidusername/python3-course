# Requirement:
# Write a program that given two numbers m and n outputs:
#   <m> + <n> = <result>
#   <m> - <n> = <result>
#   <m> * <n> = <result>
#   <m> / <n> = <result>
# If n is 0 print a message indicating that the last operation cannot be
# executed.

# Implemented on Python 3.

m = float(input('Enter m: '))
n = float(input('Enter n: '))

print(str(m) + ' + ' + str(n) + ' = ' + str(m + n))

print(str(m) + ' - ' + str(n) + ' = ' + str(m - n))

print(str(m) + ' * ' + str(n) + ' = ' + str(m * n))

if n:
    print(str(m) + ' / ' + str(n) + ' = ' + str(m / n))
else:
    print("It's not possible to divide a number by 0.")
