# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    sum_=0
    l=1
    while sum_<n:
        k=n-sum_
        if k<=2*l:
            sum_=sum_+k
            summands.append(k)
        else:
            sum_=sum_+l
            summands.append(l)
            l=l+1

    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
