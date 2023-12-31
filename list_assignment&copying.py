list1 = [10, 2, 3.4, 5.1, 6, 7, 8, 9]
list2 = list1
list1[0] = "hello"
print(list1)
print(list2)


list3 = list1.copy()
print(list3)
list1[0] = "bye"
print(list1)

result = [x**2 for x in range(10)]
print(result)

