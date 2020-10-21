import sys

try:
    x= int(input("X :"))
    y= int(input("y: "))
except ValueError:
    print("Error: invalid inout.")
    sys.exit(1)

try:
    result = x /y
except ZeroDivisionError:
    print("Error: cannot divide by zero")
    sys.exit(1)

print(f"{x} / {y} is + {result}")
