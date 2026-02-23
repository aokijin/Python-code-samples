# Sample: Sum numbers until a negative number is entered (sentinel value)
total_sum = 0
num = 0
while num >= 0:
    num_str = input("Enter a number (negative to quit): ")
    try:
        num = int(num_str)
        if num >= 0:
            total_sum += num
    except ValueError:
        print("Invalid input. Please enter an integer.")
        num = 0 # Reset num to continue loop if input is invalid

print(f"The sum of positive numbers is: {total_sum}")