#Uses python3

import sys

def negative_cycle(adj, cost, n):
    #write your code here
    dis = [0 for i in range(n)]
    for i in range(n):
        relax = 0
        for j in range(n):
            for k in range(len(adj[j])):
                if dis[adj[j][k]] > dis[j] + cost[j][k]:
                    dis[adj[j][k]] = dis[j] + cost[j][k]
                    relax = 1
        if relax == 0:
            break
    if relax == 1:
        return 1
    return 0

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
    print(negative_cycle(adj, cost, n))
