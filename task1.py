def caching_fibonacci():
    # Initialising cache
    cache = {}

    # Inner recursive function to iterate on fibonacci numbers
    def fibonacci(n: int) -> int:

        if not isinstance(n, int):
            print(f"Passed value must be an integer! Instead got '{n}'")
            return -1

        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


def main():
    # Getting fibonacci function
    fib = caching_fibonacci()

    # Usage of function
    print(fib(3))
    print(fib(6))
    print(fib(10))
    print(fib(15))

    # Trying to break logic
    print(fib("1"))
    print(fib("One"))
    print(fib(""))
    print(fib(0.5))
    print(fib([1, 2, 3]))
    print(fib({1: 1, 2: 2}))


if __name__ == '__main__':
    main()
