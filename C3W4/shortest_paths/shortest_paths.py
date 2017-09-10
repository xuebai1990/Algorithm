#Uses python3

import sys
import queue

def shortet_paths(adj, cost, s, distance, reachable, shortest):
    #write your code here
    distance[s] = 0
    reachable[s] = 1
    nq = queue.Queue()
    q = []
    visit = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        relax = 0
        for j in range(len(adj)):
            for k in range(len(adj[j])):
                if distance[adj[j][k]] > distance[j] + cost[j][k]:
                    distance[adj[j][k]] = distance[j] + cost[j][k]
                    reachable[adj[j][k]] = 1
                    relax = 1
                    if i == len(adj) - 1:
                        nq.put(adj[j][k])
                        q.append(adj[j][k])
                        visit[adj[j][k]] = 1
        if relax == 0:
            break
    if not nq.empty():
       bfs(adj, visit, nq, q)
       for i in q:
           shortest[i] = 0
    pass

def bfs(adj, visit, nq, q):
    while not nq.empty():
        x = nq.get()
        for i in adj[x]:
            if visit[i] == 0:
                visit[i] = 1
                q.append(i)
                nq.put(i)

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
    s = data[0]
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

