# Uses python3
import sys

def get_majority_element(a, left, right):
    if left + 1 == right:
        return a[left]
    #write your code here
    ave = (left + right) // 2
    m = get_majority_element(a,left,ave)
    n = get_majority_element(a,ave,right)
    if m == n:
        return m
    num_m = 0
    num_n = 0
    cri = (right - left) // 2
    for i in range(left,right):
        if a[i] == m:
            num_m += 1
        if a[i] == n:
            num_n += 1
    if num_m > cri:
        return m
    if num_n > cri:
        return n
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
