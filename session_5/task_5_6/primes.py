from math import sqrt


def get_primes_list(number: int) -> list:
    primes = [2]

    marked = [False] * (int(number / 2) + 100)

    for i in range(1, int((sqrt(number) - 1) / 2) + 1):
        for j in range((i * (i + 1)) << 1, int(number / 2) + 1, 2 * i + 1):
            marked[j] = True

    for i in range(1, int(number / 2)):
        if not marked[i]:
            primes.append(2 * i + 1)

    return primes


if __name__ == "__main__":
    print(get_primes_list(4))
    print(get_primes_list(6))
    print(get_primes_list(8))
    print(get_primes_list(38))
    print(get_primes_list(100))
