def sortStack(stack):
    # Write your code here.
    if not len(stack):
        return stack
    top = stack.pop()
    sortStack(stack)  # This will eventually be empty
    # Insert the top into the stack with order
    insertWithorder(stack, top)

    return stack


def insertWithorder(stack, value):
    # if nothing in the stack or the value is less than the top of the stack, insert it
    if not len(stack) or stack[-1] <= value:
        stack.append(value)
        return
    # Get rid of the top to open up the stack
    top = stack.pop()
    # Recursively call the function until the value is appended by either one of the two conditions
    insertWithorder(stack, value)
    # Reinsert the top
    stack.append(top)


if __name__ == "__main__":
    input_stack = [-5, 2, -2, 4, 3, 1]
    print(sortStack(input_stack))
