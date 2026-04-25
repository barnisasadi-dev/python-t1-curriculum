# Problem 1
# Use a while loop to print the word "Python" 4 times.
count = 0
while count < 4:
    print("Python")
    count += 1 


# Problem 2
# Use a while loop to print the even numbers from 2 to 12 (inclusive).

number = 2
while number <= 12:
    print(number)
    number += 2

# Problem 3
# Ask the user to input a positive number.
# Use a while loop to count up from 0 to that number (inclusive), printing each number.

while True:
    try:
        user_input = int(input("Please enter a positive number: "))
        if user_input < 0:
            print("The number must be positive. Try again.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

counter = 0


# Problem 4
# Ask the user to enter a starting number greater than 10.
# Use a while loop to count down by 5 each time until the number is less than 0.

while True:
    try:
        start_number = int(input("Enter a starting number greater than 10: "))
        if start_number > 10:
            break
        else:
            print("The number must be greater than 10. Please try again.")
    except ValueError:
        print("Invalid input. Please enter an integer.")
print(f"Countdown from {start_number}:")
while start_number > 0:
    print(start_number)
    start_number -= 1

# Problem 5
# Create a list of your three favorite animals.
# Use a while loop to print each animal with the text "is awesome!" after it.
