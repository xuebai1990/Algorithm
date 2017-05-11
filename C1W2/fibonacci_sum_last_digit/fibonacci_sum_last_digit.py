# Uses python3
import sys

def fibonacci_sum(n):
    if n <= 1:
        return n

    x=n%60
    y=n//60
    f0=0
    f1=1
    sum=1
    sum1=1
    for i in range(2,60):
        f2=(f0+f1)%10
        f0=f1
        f1=f2
        sum=(sum+f2)%10
        if i<=x:
            sum1=(sum1+f2)%10
 
    sum2=(y*sum)%10   
    if x==0:
        return sum2
    else:
        return (sum2+sum1)%10

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum(n))
