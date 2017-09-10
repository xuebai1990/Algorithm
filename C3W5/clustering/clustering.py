#Uses python3
import sys
import math

def siftdown(i, a, b, c, n):
    j = i
    nn = n // 2
    while j <= nn - 1:
        maxid = j
        l = 2 * j + 1
        if l < n and a[l] > a[maxid]:
            maxid = l
        r = 2 * j + 2
        if r < n and a[r] > a[maxid]:
            maxid = r
        if j == maxid:
            break
        else:
            a[j], a[maxid] = a[maxid], a[j]
            b[j], b[maxid] = b[maxid], b[j]
            c[j], c[maxid] = c[maxid], c[j]
            j = maxid

def heap_sort(a, b, c):
    n = len(a)
    n2 = n // 2
    for i in range(n2 - 1, -1, -1):
        siftdown(i, a, b, c, n)
    nn = n
    for i in range(n - 1):
        a[0], a[nn - 1] = a[nn - 1], a[0]
        b[0], b[nn - 1] = b[nn - 1], b[0]
        c[0], c[nn - 1] = c[nn - 1], c[0]
        nn = nn - 1
        siftdown(0, a, b, c, nn)

def find(i, parent):
    if i != parent[i]:
        parent[i] = find(parent[i], parent)
    return parent[i]

def union(i, j, parent, rank):
    if rank[i] > rank[j]:
        parent[j] = i
    else:
        parent[i] = j
        if rank[i] == rank[j]:
            rank[j] += 1

def clustering(x, y, k, n):
    #write your code here
    edge = []
    st = []
    ed = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            edge.append((x[i]-x[j])**2+(y[i]-y[j])**2)
            st.append(i)
            ed.append(j)
    heap_sort(edge, st, ed)
    parent = [i for i in range(n)]
    rank = [0 for i in range(n)]
    num = n
    for i in range(len(edge)):
        x = find(st[i], parent)
        y = find(ed[i], parent)
        if x != y:
            if num == k:
                return math.sqrt(edge[i])
            union(x, y, parent, rank)
            num -= 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k, n)))
