# functions
# Function to assess input is a digit
# error if input is string

# Function
# ask questions and assess answer against correct number
error = "Question failed, please restart"

print("Question 1")
answer = int(input("8 * 2 * 3="))
if answer == 48:
    print("Correct proceed to the next question")
else:
    print(error)

print("Question 2")
answer = int(input("69 * 364="))
if answer == 23296:
    print("Correct proceed to the next question")
else:
    print(error)

print("question 3")
answer = int(input("445 * 156="))
if answer == 69420:
    print("correct proceed to the next question")
else:
    print(error)

print("question 4")
answer = int(input("2(1 + 2)"))
