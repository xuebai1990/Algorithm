# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def dp_sequence(n):
    sequence = []
    sequence.append(n)
    if n == 1:
        return(sequence)
    min_op = (n + 1) * [0]
    n_op = (n + 1) * [0]
    min_op[1] = 0
    for i in range(2, n + 1):
        a = n
        b = n
        if i % 3 == 0:
            a = min_op[i // 3] + 1
        if i % 2 == 0:
            b = min_op[i // 2] + 1
        c = min_op[i - 1] + 1
        min_op[i] = min(a, b, c)
        if min_op[i] == a:
            n_op[i] = 1
        elif min_op[i] == b:
            n_op[i] = 2
        else:
            n_op[i] = 3
    x = n
    while x > 1:
        if n_op[x] == 1:
            sequence.append(x // 3)
            x = x // 3
        elif n_op[x] == 2:
            sequence.append(x // 2)
            x = x // 2
        else:
            sequence.append(x - 1)
            x = x - 1
    return reversed(sequence)

input = sys.stdin.read()
n = int(input)
sequence = list(dp_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
