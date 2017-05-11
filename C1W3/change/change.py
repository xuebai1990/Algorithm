# Uses python3
import sys

def get_change(m):
    #write your code here
    sum_=0
    coin=[10,5,1]
    i=0
    num=0
    for i in range(0,3):
        while sum_<m and (m-sum_)>=coin[i]:
            sum_=sum_+coin[i]
            num=num+1

    return num

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
