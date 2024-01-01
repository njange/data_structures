stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

# Remove the last item from the list
stack.pop()
print(stack)

# Length of the list
print(len(stack))

# Check if the list is empty
print(not stack)

# Access the last item
print(stack[-1])

# Remove all items from the list
stack.clear()
print(stack)


# Complete example of stack
stack1 = []
def push():
    element = input("Enter the element to be pushed: ")
    stack1.append(element)
    print(stack1)

def pop_element():
    if not stack1:
        print("Stack is empty")
    else:
        e = stack1.pop()
        print("Removed element: ", e)
        print(stack1)

while True:
    print("Select the operation 1.push 2.pop 3.quit")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("Enter the correct choice")
