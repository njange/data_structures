num = [10, 20, 5, 7, 1, 3]

# Sort the list in ascending order
num.sort()
print(num)

# Sort the list in descending order
num.sort(reverse=True)
print(num)

list1 = ["aa", "b", "ccc", "dddd", ]
list1.sort()
print(list1)

# Sort by length of the string
list1.sort(key=len)
print(list1)

list2 = [[1, 6], [4, 5], [3, 4]]
print(list2)

list2.sort()
print(list2)

# Sort by the second item in the sublist
def second_item(x):
    return x[1]
list2.sort(key=second_item)
print(list2)

def SortBySec(element):
    return element[1]
list2.sort(key=SortBySec)
print(list2)

# Sort by the sum of the sublist
def sum_list(x):
    return sum(x)
list2.sort(key=sum_list)
print(list2)

# Using sorted method
list1 = ["aa", "b", "ccc", "dddd", "e"]
tuple1 = ((10, 20), (5, 7), (1, 3))
print(sorted(list1))
print(list1)
print(sorted(tuple1))
print(tuple1)
