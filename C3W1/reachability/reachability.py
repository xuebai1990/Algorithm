#Uses python3

import sys

def reach(adj, x, y, n):
    #write your code here
    visit = [0 for _ in range(n)]
    explore(adj, x, visit)
    if visit[y] == 0:
        return 0
    else:
        return 1

def explore(adj, v, visit):
    for i in adj[v]:
        if visit[i] == 0:
            visit[i] = 1
            explore(adj, i, visit)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y, n))
