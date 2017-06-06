# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
    while left<right:
        mid=(left+right)//2
        if a[mid]==x:
            return mid
        elif x<a[mid]:
            right=mid
        else:
            left=mid+1
    return -1

def sort(a, b, c, d, l, r):
    if (r - l) <= 1:
        return
    ave = (l + r) // 2
    sort(a, b, c, d, l, ave)
    sort(a, b, c, d, ave, r)
    merge(a, b, c, d, l, ave, r)
    for i in range(l, r):
        a[i] = c[i]
        b[i] = d[i]
    return

def merge(a, b, c, d, l, ave, r):
    i0 = l
    i1 = ave
    for i in range(l, r):
        if i0 < ave and (i1 >= r or a[i0] <= a[i1]):
            c[i] = a[i0]
            d[i] = b[i0]
            i0 = i0 + 1
        else:
            c[i] = a[i1]
            d[i] = b[i1]
            i1 = i1 + 1
    return

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    a = []
    b = []
    for i in range(0, len(starts)):
        a.append(starts[i])
        b.append(1)
    for i in range(0, len(ends)):
        a.append(ends[i])
        b.append(2)
    for i in range(0, len(points)):
        a.append(points[i])
        b.append(3)
    c = [0] * len(a)
    d = [0] * len(a)
    sort(a, b, c, d, 0, len(a))
    nums = 0
    nume = 0
    for i in range(0, len(a)):
        if b[i] == 1:
            nums += 1
        if b[i] == 2:
            nume += 1
        if b[i] == 3:
            seg = nums - nume
            n = binary_search(points, a[i])
            cnt[n] = seg
    return cnt

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
