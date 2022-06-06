import sys
import os


print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What are tuples contained in?")
if answer.lower() == "parenthesis":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


answer = input("What is a changeable,unordered collection of unique key:value pairs?")
if answer.lower() == "dictionary":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("what data structure is made up of brackets?")
if answer.lower() == "list":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("What is the first element that a computer counts from?")
if answer.lower() == "zero":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("A boolean operator states what?")
if answer.lower() == "true and false":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("String slicing counts from what number?")
if answer.lower() == "zero":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("What is a block of code which executes only when it is called?")
if answer.lower() == "function":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("What are information being sent back to the function?")
if answer.lower() == "arguments":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

print("You got " + str(score) + "questions correct")
print("You got " + str((score/8) * 100) + "%.")