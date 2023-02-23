def print_fibonacci(length):
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length == 2:
        print([0, 1])
    else:
        a, b = 0, 1
        fib_sequence = [a, b]
        while len(fib_sequence) < length:
            a, b = b, a + b
            fib_sequence.append(b)
        print(fib_sequence)