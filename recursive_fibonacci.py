def fibonacci(n):
    if n == 0:
        return 0      # Base case 1
    elif n == 1:
        return 1      # Base case 2
    else: 
        return fibonacci(n-1) + fibonacci(n-2)    # Recursive Case
        
#User input
num = int(input("Enter a nummber: "))
print("Fibonacci of", num, "is", fibonacci(num))