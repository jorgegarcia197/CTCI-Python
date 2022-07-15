

def isPrime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


factors = [1]


def get_max_prime_factor(number):

    for i in range(2, number//2+1):
        if number % i == 0:
            if isPrime(i):
                factors.append(i)
    print("Largest Prime Factor =", max(factors))


if __name__ == "__main__":
    number = 600851475143
    print(get_max_prime_factor(number))
