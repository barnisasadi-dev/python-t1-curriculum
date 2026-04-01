# Problem 1
# Find and print the sum of all the numbers greater than 25 in the list.
numbers = [10, 32, 27, 8, 50]
total = 0
for num in numbers:
    if num > 25:
        total += num
print("The sum of numbers greater than 25 is:", total)


# Problem 2
# Find and print the sum of all the numbers less than -10 in the list.
numbers = [-5, -20, -11, 0, 4, -15]
total = 0
for num in numbers:
    if num < -10:
        total += num
print("The sum of numbers less than -10 is:", total)


# Problem 3
# Find and print the biggest number less than 100 in the list.
numbers = [104, 99, 86, 120, 101]
less_than_100 = [num for num in numbers if num < 100]
if less_than_100:
    biggest = max(less_than_100)
    print("The biggest number less than 100 is:", biggest)
else:
    print("No numbers less than 100 found.")


# Problem 4
# Find and print the biggest number in the list.
numbers = [12, 7, 33, 5]
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num
print("The biggest number is:", biggest)


# Problem 5
# Find and print the total sum of all the numbers in the list.
numbers = [1, 3, 5, 7, 9]
total = 0 
for num in numbers:
    total += num
print("The total sum is:", total)




