'''#bai 1
with open("user-inputs.txt",'w') as f:
    lines =[]
    while True:
        line = input("Enter your input (or press Enter to quit): ")
        if line == "":
            if not lines :
                print("No input provided")
                continue
            else :
                break
        lines.append(line + "\n")
print("Nội dung file user-inputs.txt :")
with open("user-inputs.txt",'r') as f :
    print(f.read())
#bai 2
import datetime

with open("user-logs.txt", 'w') as f:
    lines = []
    while True:
        line = input("Enter your input (or press Enter to quit): ")
        if line == "":
            if not lines:
                print("No input provided")
                continue
            else:
                break
        lines.append(line + "\n")

    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"[{current_time}]\n")
    f.writelines(lines)
    f.write("\n")

print("Nội dung file user-logs.txt :")
with open("user-logs.txt", 'r') as f:
    print(f.read())'''
#bai 3
with open("question-bank.txt", 'r') as f:
    questions = [line.strip().split(',') for line in f.readlines() if line.strip()]

print("Give the correct answers to get points.")
score = 0
total_questions = len(questions)

for question, answer in questions:
    user_answer = input(f"{question}: ")
    if user_answer.strip() == answer.strip():
        score += 1
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {answer}")

print(f"== You got {score}/{total_questions} points ==")



