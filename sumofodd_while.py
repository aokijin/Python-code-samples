num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

total = 0
current = num1

while current <= num2:
    if current % 2 != 0:
        total += current
    current += 1
    
print("Sum of odd numbers: ", total)