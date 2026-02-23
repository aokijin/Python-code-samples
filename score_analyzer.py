scores = []

print("Please enter 5 quiz scores: ")

for i in range(5):
    score = int(input(f"Enter score {i+1}: "))
    scores.append(score)
    
total_score = 0

print(("\n--- All Scores ---"))

for s in scores:
    print(s)
    total_score += s
    
average = total_score / 5
print (f"Total Score: {total_score}")
print(f"Average Score: {average}")

if average >= 75:
    print("Status: Passed")
else:
    print("Status: Failed")