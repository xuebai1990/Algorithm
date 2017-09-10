#Uses python3

import sys


def acyclic(adj, n):
    visit = [0 for i in range(n)]
    for i in range(n):
        if visit[i] == 0:
            explore(adj, i, visit)
            if visit[i] == 1:
                return 1
            else:
                visit[i] = 1
    return 0

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
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))
