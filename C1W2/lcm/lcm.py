# Uses python3
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        c=a%b
        return gcd(b,c)

def lcm(a, b):
    x=gcd(a,b)
    return a*b//x    

if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

