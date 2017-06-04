#Uses python3
import sys
import math
import random

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

def partition2(a, b, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]
    a[l], a[j] = a[j], a[l]
    b[l], b[j] = b[j], b[l]
    return j


def randomized_quick_sort(a, b, l, r):
    if l >= r:
        return
    k = random.randint(l, r - 1)
    a[l], a[k] = a[k], a[l]
    b[l], b[k] = b[k], b[l]
    m = partition2(a, b, l, r)
    randomized_quick_sort(a, b, l, m);
    randomized_quick_sort(a, b, m + 1, r);

def dis(xx1, yy1, xx2, yy2):
    return (xx1 - xx2)**2+(yy1 - yy2)**2

def minimum_distance(x1, y1, x2, y2, l, r):
    #write your code here
    if (r - l) == 2:
        return dis(x1[l], y1[l], x1[l+1], y1[l+1])
    if (r - l) == 3:
        a1 = dis(x1[l], y1[l], x1[l+2], y1[l+2])
        a2 = dis(x1[l+1], y1[l+1], x1[l+2], y1[l+2])
        a3 = dis(x1[l], y1[l], x1[l+1], y1[l+1])
        return min(a1, a2, a3)
    ave = (l + r) // 2
    num = len(x2)
    pxl = []
    pyl = []
    pxr = []
    pyr = []
    for i in range(0, num):
        if x2[i] < x1[ave]:
            pxl.append(x2[i])
            pyl.append(y2[i])
        else:
            pxr.append(x2[i])
            pyr.append(y2[i])    
    d1 = minimum_distance(x1, y1, pxl, pyl, l, ave)
    d2 = minimum_distance(x1, y1, pxr, pyr, ave, r)
    dmin = min(d1, d2)
    stripx = []
    stripy = []
    for i in range(0, num):
        if abs(x2[i] - x1[ave]) < dmin:
            stripx.append(x2[i])
            stripy.append(y2[i])
    nn = len(stripx)
    for i in range(0, nn):
        for j in range(i + 1, nn):
            if abs(stripy[i] - stripy[j]) > dmin:
                break
            d = dis(stripx[i], stripy[i], stripx[j], stripy[j])
            if d < dmin:
                dmin = d
    return dmin

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    x1 = x
    y1 = y
    x2 = x
    y2 = y
    xx = n * [0]
    yy = n * [0]
    sort(x1, y1, xx, yy, 0, len(x1))
    sort(y2, x2, yy, xx, 0, len(y2))
    print("{0:.9f}".format(math.sqrt(minimum_distance(x1, y1, x2, y2, 0, len(x1)))))
