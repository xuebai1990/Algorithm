#Uses python3

import sys

def greatequal(a,b):
    i=0
    c=a
    d=b
    while c!=0:
        c=c//10
        i=i+1
    j=0
    while d!=0:
        d=d//10
        j=j+1
    x=a*10**j+b
    y=b*10**i+a
    if x>=y:
        return 1
    else:
        return 0

def largest_number(a):
    #write your code here
    b=""
    while len(a)!=0:
        maxd=0
        ind=0
        rei=0
        for i in a:
            re=greatequal(int(i),int(maxd))
            if re==1:
                maxd=i
                rei=ind
            ind=ind+1
        b=b+maxd
        del a[rei]           
    return b

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
