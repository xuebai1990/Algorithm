# python3
import random

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash(s, p, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % p
    return ans % p

def pre_hash(T, P, prime, x, H):
    l = len(T) - len(P) + 1
    s = T[(l - 1):len(T)]
    H[l - 1] = hash(s, prime, x)
    y = 1
    for i in range(len(P)):
        y = (y * x) % prime
    for i in range(l - 2, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + len(P)])) % prime

def get_occurrences(pattern, text):
    p = 1000000007
    x = random.randint(1, p - 1)
    result = []
    pHash = hash(pattern, p, x)
    H = [0 for i in range(len(text) - len(pattern) + 1)]
    pre_hash(text, pattern, p, x, H)
    for i in range(len(text) - len(pattern) + 1):
        if pHash != H[i]:
            continue
        st = text[i:(i+len(pattern))]
        if st == pattern:
            result.append(i)
    return result

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

