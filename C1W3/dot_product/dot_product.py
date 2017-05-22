#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if a[j-1]<a[j]:
#                tmp=a[j]
#                a[j]=a[j+1]
#                a[j+1]=a[j]
                a[j-1],a[j]=a[j],a[j-1]
            if b[j-1]<b[j]:
#                tmp=b[j]
#                b[j]=b[j+1]
#                b[j+1]=tmp
                b[j-1],b[j]=b[j],b[j-1]
#    print a
#    print b
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
