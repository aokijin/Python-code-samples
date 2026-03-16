def countdown(n):
    # Base Case (Stops Recursion)
    if n == 0:
        return
    print(n)
    # Recursive Case (Calls Itself with smaller value)
    countdown(n-1)
    
number = int(input("Enter a number: "))
countdown(number)