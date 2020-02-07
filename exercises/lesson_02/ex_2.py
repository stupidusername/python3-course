# Requirement:
# Write a program that checks if three given (x, y) points are collinear.
# Assume that x and y are integers.

# Implemented on Python 3.

# Point A.
x = float(input('Enter Ax: '))
y = float(input('Enter Ay: '))
a = (x, y)

# Point B.
x = float(input('Enter Bx: '))
y = float(input('Enter By: '))
b = (x, y)

# Point C.
x = float(input('Enter Cx: '))
y = float(input('Enter Cy: '))
c = (x, y)

# Check if the area of the triangle determined by the three points is 0.
# The area of this triangle is determined by
# .5 * |Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By)|.
det = abs(a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1]))

# det is a float value. We need to check if it's close enough to 0.
threshold = .000001

if det < threshold:
    print('The points are collinear.')
else:
    print('The points are not collinear.')
