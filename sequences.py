numbers = [10,20,5,7,1,3]
numbers2 = (8,3,9,2,5)
name = "John"

#Length operation

print(len(name))
print(len(numbers))
print(len(numbers2))

#Length operation is used to find the number of elements in the sequence

#Select operation
print(numbers[0])
print(numbers2[1])
print(name[2])
#Select operation is used to select a single element

#Slice operation
print(numbers[0:3])
print(numbers2[1:4])
print(name[2:4])
#Slice operation is used to select a range of elements

#Count operation
print(numbers.count(5))
print(numbers2.count(5))
print(name.count("h"))
#Count operation is used to count the number of occurences of the element

#Index operation
print(numbers.index(5))
print(numbers2.index(5))
print(name.index("h"))
#Index operation is used to find the index of the first occurence of the element.


#Membership operation
print(5 in numbers)
print(5 in numbers2)
print("a" in name)
#Membership operation is used to check if the element is present in the sequence.

#Concatenation operator
print(numbers + [4,5,6])
print(numbers2 + (4,5,6))
print(name + " Doe")
#Concatenation operator is used to join two sequences.

#Repetition operator
print(numbers * 2)
print(numbers2 * 2)
print(name * 2)
#Repetition operator is used to repeat the elements of the sequence.

#Max operation
print(max(numbers))
print(max(numbers2))
print(max(name))

#Sum operator
print(sum(numbers))
print(sum(numbers2))
