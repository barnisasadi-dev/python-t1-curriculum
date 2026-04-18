# Problem 1
# Write a function that returns the number 42 and print the result.
def answer():
    return 42
print(answer())

# Problem 2
# Write a function that returns "penguin" and print the result.
def get_penguin():
    return "penguin"
result = get_penguin()
print(result)

# Problem 3
# Create a variable for a fruit, then print it.
# Modify it inside a function and print it again.

fruit = "apple"
print("Original fruit:", fruit)
def modify_fruit():
    global fruit
    print("Inside function, modified fruit:", fruit)
    modify_fruit()
    print("After function call, fruit:", fruit)


# Problem 4
# Write a function that takes two parameters: first_name and last_name.
# The function should return a string that combines the first and last names separated by a space.

def print_and_modify_name(first_name, last_name):
    first_name = first_name.upper()
    full_name = f"{first_name} {last_name}"
    print("Full Name:", full_name)
original_first_name = "John"
last_name = "Doe"
modified_first_name = print_and_modify_name(original_first_name, last_name)
print("Original first name outside function:", original_first_name)
print("Modified first name returned from function:", modified_first_name)


# Problem 5
# Write a function called calculate_perimeter that takes two parameters: length and width.
# The function should return the perimeter of a rectangle (2 * (length + width)).

def calculate_perimeter(length, width):
    """
    Calculate the perimeter of a rectangle.

    Parameters:
    length (float or int): The length of the rectangle.
    width (float or int): The width of the rectangle.

    Returns:
    float: The perimeter of the rectangle.
    """
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == "__main__":
    # Example rectangle dimensions
    length = 10
    width = 5

    result = calculate_perimeter(length, width)
    print(f"The perimeter of the rectangle with length {length} and width {width} is {result}.")









