# Uses python3
import sys
import random

def partition3(a, l, r):
    #write your code here
    if r - l <= 1:
        if a[l] > a[r]:
            a[l], a[r] = a[r], a[l]
            return l, r

    x = a[l]
    lt = l
    rt = r
    i = l

    while i <= rt:
        if a[i] < x:
            a[i],a[lt] = a[lt], a[i]
            lt += 1
            i += 1
        elif a[i] > x:
            a[i],a[rt] = a[rt], a[i]
            rt -= 1
        else:
            i += 1

    a[l], a[lt] = a[lt], a[l]
    return lt, rt

def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m, n = partition3(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, n + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
