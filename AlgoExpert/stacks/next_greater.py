# O(n2) and O(n) space

def nextGreaterElement(array):
    # Write your code here.
    output = []
    for i in range(len(array)):
        ref = array[i]
        counter = i+1
        while counter >= 0:
            idx = counter % len(array)
            if idx == i:
                output.append(-1)
                break
            elif array[idx] > ref:
                output.append(array[idx])
                break
            counter += 1
    return output


def nextGreaterElement_2(array):
    stack = []
    output = [-1] * len(array)
    for idx in range(2*len(array)):
        circular_idx = idx % len(array)
        while stack and array[stack[-1]] < array[circular_idx]:
            output[stack.pop()] = array[circular_idx]
        stack.append(circular_idx)
    return output


if __name__ == "__main__":
    input_list = [2, 5, -3, -4, 6, 7, 2]
    print(nextGreaterElement_2(input_list))
