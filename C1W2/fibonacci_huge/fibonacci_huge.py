# Uses python3
import sys

def findT(m):
    f0=0
    f1=1
    for i in range(0,m*m):
        f2=(f0+f1)%m
        f0=f1
        f1=f2
        if f0==0 and f1==1:
            return i+1

def get_fibonacci_huge(n, m):
    if n <= 1:
        return n

    period=findT(m)
    x=n%period

    f0=0
    f1=1
    for i in range(0,x-1):
        f2=(f0+f1)%m
        f0=f1
        f1=f2

    return f2 % m

if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(get_fibonacci_huge(n, m))
