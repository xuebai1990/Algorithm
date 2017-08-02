#Uses python3

import sys


def number_of_components(adj, n):
    result = 0
    visit = [0 for i in range(n)]
    #write your code here
    for i in range(n):
        if visit[i] == 0:
            explore(adj, i, visit)
            result += 1
    return result

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
        adj[b - 1].append(a - 1)
    print(number_of_components(adj, n))
