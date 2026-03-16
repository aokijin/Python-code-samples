def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]
        
#User input
text = (input("Enter a string: "))
print("Reversed string:", reverse_string(text))
