# functions
error = "Question failed, please restart"

# main program
print("welcome to the challenger")

show_instructions = input("have you played this quiz before").lower().strip()
if show_instructions == "no" or show_instructions == "n":
        print("""this quiz is here to test your knowledge
        *** tips ***
        tip #1 *= multiplication
        tip #2 /= division
        tip #3 -= subtraction
        tip #4 += addition
        thanks for testing your knowledge on our quiz""")

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
