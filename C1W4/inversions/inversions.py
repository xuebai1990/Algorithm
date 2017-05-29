# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions += merge(a, b, left, ave, right)
    for i in range(left,right):
        a[i]=b[i]   
    return number_of_inversions

def merge(a, b, left, ave, right):
    num = 0
    i0=left
    i1=ave
    for i in range(left,right):
        if i0<ave and (i1>=right or a[i0]<=a[i1]):
            b[i]=a[i0]
            i0=i0+1
        else:
            b[i]=a[i1]
            i1=i1+1
            num = num + (ave - i0)      
    return num

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
