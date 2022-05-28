def arrayOfProducts(array):
    # Write your code here.
    output = []
    for idx in range(len(array)):
        left_products = 1
        right_products = 1
        left = idx-1
        right = idx+1
        while left >= 0:
            left_products *= array[left]
            left -= 1
        while right < len(array):
            print(array[right])
            right_products *= array[right]
            right += 1
        output.append(left_products*right_products)
    return output


if __name__ == '__main__':
    array = [5, 1, 4, 2]
    print(arrayOfProducts(array))
