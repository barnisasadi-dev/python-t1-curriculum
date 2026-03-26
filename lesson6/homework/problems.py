# Problem 1
# Count and print how many times "Alex" appears in the list.
names = ["Liam", "Alex", "Sophie", "Alex", "Mia"]
print(names) 
alex_count = names.count("Alex")
print(f"'Alex' appears {alex_count} times in the list.")



# Problem 2
# Search for "elephant" in the list and print if it's found.
animals = ["zebra", "giraffe", "lion", "tiger"]
print(animals)
if "elephant" in animals:
    print("found elephant")
else:
    print("elephant not found")
     

# Problem 3
# Count and print how many scores are 100.
scores = [95, 100, 88, 100, 77, 92]
print(scores)
count_100 = scores.count(100)
print(f"Number of scores that are 100: {count_100}")


# Problem 4
# Search for the color "blue" in the list and print its index if it's found.
colors = ["red", "green", "blue", "yellow"]
print(colors)
search_color = "blue"
if search_color in colors:
    index = colors.index(search_color)  # Get the index of the first occurrence
    print("The color '" + search_color + "' is found at index", index)
else:
    print("The color '" + search_color + "' is not in the list")


# Problem 5
# Count and print how many temperatures in the list are below zero.
temperatures = [3, -2, 5, -7, 0, 4, -1]
print(temperatures)
count_below_zero = 0
for temp in temperatures:
    if temp < 0:       
        count_below_zero += 1  
        print("Number of temperatures below zero:", count_below_zero)