import  sys

x= int(input("X :"))
y= int(input("y: "))

try:
    result = x /y
except ZeroDivisionError:
    print("Error: cannot divide by zero")
    sys.exit(1)

print(f"{x} / {y} is + {result}")