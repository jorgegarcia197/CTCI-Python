def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)


if __name__ == "__main__":
    print(getNthFib(6))
