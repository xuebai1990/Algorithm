#Uses python3

import sys

sys.setrecursionlimit(200000)

clock = 0

def siftdown(i, a, b, n):
    j = i
    nn = n // 2
    while j <= nn - 1:
        maxid = j
        l = 2 * j + 1
        if l < n and a[l] < a[maxid]:
            maxid = l
        r = 2 * j + 2
        if r < n and a[r] < a[maxid]:
            maxid = r
        if j == maxid:
            break
        else:
            a[j], a[maxid] = a[maxid], a[j]
            b[j], b[maxid] = b[maxid], b[j]
            j = maxid

def heap_sort(a, b):
    n = len(a)
    n2 = n // 2
    for i in range(n2 - 1, -1, -1):
        siftdown(i, a, b, n)
    nn = n
    for i in range(n - 1):
        a[0], a[nn - 1] = a[nn - 1], a[0]
        b[0], b[nn - 1] = b[nn - 1], b[0]
        nn = nn - 1
        siftdown(0, a, b, nn)

def explore(adj, used, order, x):
    global clock
    for i in adj[x]:
        if used[i] == 0:
            used[i] = 1
            explore(adj, used, order, i)
    clock += 1
    order[x] = clock

def dfs(adj, used, order):
    #write your code here
    for i in range(len(adj)):
        if used[i] == 0:
            used[i] = 1
            explore(adj, used, order, i)

def number_of_strongly_connected_components(adj, rev_adj):
    result = 0
    #write your code here
    order = [0 for i in range(len(adj))]
    used = [0 for i in range(len(adj))]
    index = [i for i in range(len(adj))]
    dfs(rev_adj, used, order)
#    print(order, index)
    heap_sort(order, index)
#    print(order, index)
    exist = [0 for i in range(len(adj))]
    abd = 0
    for i in index: 
        if exist[i] == 0:
            exist[i] = 1
            explore(adj, exist, order, i) 
            result += 1  
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        rev_adj[b - 1].append(a - 1)
    print(number_of_strongly_connected_components(adj, rev_adj))
