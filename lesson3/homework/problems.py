# Problem 1
# Ask the user to enter a number.
# Print "Even" if the number is divisible by 2, otherwise print "Odd".
A = int(input("enter a number"))
if A % 2 == 0:
    print("even")
else:
    print ("odd")

# Problem 2
# Ask the user for the day of the week (all lowercase).
# Print "Weekend" if the day is "saturday" or "sunday",
# else print "Weekday".
week = input("what day is today")
if week == "saturday" or week == "sunday" :
    print ("its weekend")
else: 
    print ("its weekday")
# Problem 3
# Generate a random number between 1 and 10 (inclusive).
# Ask the user to guess the number.
# Print "Correct!" if the guess matches the random number, else print "Try again!".



# Problem 4
# Ask the user for a positive integer.
# If the number is divisible by 2 and greater than 10, print "Big even number".
# Otherwise print "Number does not meet criteria".
a = int(input("enter a positive number"))
if a % 2 > 10:
    print("big even number")
else:
    print("number does not meet criteria")


# Problem 5
# Ask the user for two numbers.
# Print which number is larger.
# If the numbers are equal, print "Numbers are equal".