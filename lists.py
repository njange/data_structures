animals = ["cat", "dog", "rabbit", "parrot"]
print(animals)

fruits = [["tomatoes", "oranges"], "apple", "banana", "cherry"]
print(fruits[0][1])

# Replace the second item
fruits[1] = "mango"
print(fruits)

animals.sort()
print(animals)

# Sort the list in descending order
numbers = [9, 1, 4, 7, 3]
numbers.sort()
print(numbers)

# Delete an item from the list
del numbers[1]
print(numbers)

# Delete the entire list
del numbers

#Insert an item at a given position
animals.insert(2, "tiger")
print(animals)

# Append an item to the end of the list
animals.append("lion")
print(animals)

# Remove the first item from the list whose value is x
animals.remove("cat")
print(animals)

# Reverse the elements of the list in place
animals.reverse()
print(animals)

fruits = ["apple", "banana", "cherry"]
print(fruits)

fruits[1]="grapes"
print(fruits)

fruits.insert(1, "orange")
print(fruits)

fruits.sort()
print(fruits)

fruits.append("mango")
print(fruits)


fruits.reverse()
print(fruits)

fruits.remove("mango")
print(fruits)

fruits.pop()
print(fruits)
