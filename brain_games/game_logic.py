def is_prime(n: int) -> bool:
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def is_even(n: int) -> bool:
    return n % 2 == 0