#Uses python3

import sys
import queue

def distance(adj, s, t):
    #write your code here
    n = len(adj)
    dis = [n for _ in range(n)]
    dis[s] = 0
    q = queue.Queue()
    q.put(s)
    while not q.empty():
        x = q.get()
        for i in adj[x]:
            if i == t:
                return dis[x] + 1
            if dis[i] == n:
                q.put(i)
                dis[i] = dis[x] + 1
    return -1

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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
