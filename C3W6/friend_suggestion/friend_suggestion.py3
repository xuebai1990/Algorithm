#!/usr/bin/python3

import sys
import queue

class MyPriorityQueue:
    def __init__(self, index, q):
        self.index = index
        self.q = q
        self.position = [i for i in range(len(self.q))]

    def siftup(self, i):
        j = i
        while self.q[j] < self.q[(j - 1) // 2]:
            self.index[j], self.index[i] = self.index[i], self.index[j]
            self.q[j], self.q[i] = self.q[i], self.q[j]
            self.position[index[j]] = i
            self.position[index[i]] = j
            j = (j - 1) // 2

    def siftdown(self, i):
        m = len(self.q)
        n = m // 2
        j = i
        while j <= n - 1:
            maxid = j
            l = 2 * j + 1
            if l < m and self.q[l] < self.q[maxid]:
                maxid = l
            r = 2 * j + 2
            if r < m and self.q[r] < self.q[maxid]:
                maxid = r
            if j == maxid:
                break
            else:
                self.index[j], self.index[maxid] = self.index[maxid], self.index[j]
                self.q[j],self.q[maxid] = self.q[maxid], self.q[j]
                self.position[index[j]] = maxid
                self.position[index[maxid]] = j
                j = maxid

    def buildq(self):
        m = len(self.q)
        n = m // 2
        for i in range(n - 1, -1, -1):
            self.siftdown(i)

    def changepriority(self, i, value):
        temp = self.q[self.position[i]]
        self.q[self.position[i]] = value
        if value > temp:
            self.siftdown(self.position[i])
        else:
            self.siftup(self.position[i])

    def extractmin(self):
        m = len(self.q)
        a, b = self.index[0], self.q[0]
        self.index[0], self.index[m - 1] = self.index[m - 1], self.index[0]
        self.q[0], self.q[m - 1] = self.q[m - 1], self.q[0]
        self.position[index[0]] = m - 1
        self.position[index[m-1]] = 0
        self.index.pop()
        self.q.pop()
        self.siftdown(0)
        return a, b

class BiDij:
    def __init__(self, n):
        self.n = n;                             # Number of nodes
        self.inf = n*10**6                      # All distances in the graph are smaller
        self.d = [[self.inf]*n, [self.inf]*n]   # Initialize distances for forward and backward searches
        self.visited = [False]*n                  # visited[v] == True iff v was visited by forward or backward search
        self.workset = []                       # All the nodes visited by forward or backward search
        self.prev = [[None]*n, [None]*n]

    def clear(self):
    """Reinitialize the data structures for the next query after the previous query."""
        for v in self.workset:
            self.d[0][v] = self.d[1][v] = self.inf
            self.visited[v] = False;
        del self.workset[0:len(self.workset)]
        self.prev = [[None]*n, [None]*n]

    def visit(self, q, side, v, cost):
    """Try to relax the distance to node v from direction side by value dist."""
        # Implement this method yourself
        for i in range(len(adj[side][v])):
            if self.d[side][adj[side][v][i]] > self.d[side][v] + cost[side][v][i]:
                self.d[side][adj[side][v][i]] = self.d[side][v] + cost[side][v][i]
                prev[adj[side][v][i]] = v
        self.workset.append(v)
        pass

    def query(self, adj, cost, s, t):
        self.clear()
        q = [queue.PriorityQueue(), queue.PriorityQueue()]
        self.d[0][s] = 0
        self.d[1][t] = 0
        while True:
        # Implement the rest of the algorithm yourself
        return -1


def readl():
    return map(int, sys.stdin.readline().split())


if __name__ == '__main__':
    n,m = readl()
    adj = [[[] for _ in range(n)], [[] for _ in range(n)]]
    cost = [[[] for _ in range(n)], [[] for _ in range(n)]]
    for e in range(m):
        u,v,c = readl()
        adj[0][u-1].append(v-1)
        cost[0][u-1].append(c)
        adj[1][v-1].append(u-1)
        cost[1][v-1].append(c)
    t, = readl()
    bidij = BiDij(n)
    for i in range(t):
        s, t = readl()
        print(bidij.query(adj, cost, s-1, t-1))
