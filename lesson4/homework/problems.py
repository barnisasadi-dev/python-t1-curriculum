# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one.
score1 = int(input("enter test scores"))
score2 = int(input("enter the second score"))
if score1 >= 50 and  score2 >= 50 :
    print("you passed both")
else:
     print("you failed at least one")

# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch = input("did you bring lunch? yes/no")
water = input("did ou bring water? yes/no")
if lunch == 'yes' and water == 'yes':
     print ("your fully ready")
elif lunch == 'yes' and water == 'no':
     print ("you're somewhat ready ")
else:
     print ("You're not ready")


# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
number = int(input("enter a number"))
if number>=1 and number<= 10 :
     print("out of range")
else:
     print("in range")


 
# Problem 4
# Generate a random number between 1 and 10.
# Ask the user to guess.
# If the guess is right AND the number is even, print "Even match!"
# Else if guess is right OR number is 5, print "Nice try!"
# Otherwise, print "Nope."
import random
num = random.randint(1, 10)
guess = int(input("guess a number"))
if guess == num and guess % 2 == 0 :
     print("Even match")
elif guess == num  or guess == 5:
     print ("Nice try")
else:
     print("Nope")


       


# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 5 == 0 and num2 % 2 != 0 :
     print ("Interesting pair!")
else:
     print("Plain pair.")