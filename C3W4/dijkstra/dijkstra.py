#Uses python3

import sys
import queue


def distance(adj, cost, s, t, n):
    #write your code here
    visit = [0 for i in range(n)]
    dis = [float('inf') for i in range(n)]
    dis[s] = 0
    for i in range(n - 1):
        xmin = float('inf')
        index = 0
        for j in range(n):
            if dis[j] < xmin and visit[j] == 0:
                xmin = dis[j]
                index = j
        visit[index] = 1
        for j in range(len(adj[index])):
            if dis[adj[index][j]] > dis[index] + cost[index][j]:
                dis[adj[index][j]] = dis[index] + cost[index][j]
    if dis[t] < float('inf'):
        return dis[t]
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t, n))
