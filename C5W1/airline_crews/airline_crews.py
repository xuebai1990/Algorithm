# python3
import queue

class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        new_adj = [[] for _ in range(n + m + 2)]
        for i in range(n):
            new_adj[0].append(i + 1)
            for j in range(m):
                if adj_matrix[i][j] == 1:
                    new_adj[i + 1].append(j + n + 1)
        for i in range(m):
            new_adj[i + n + 1].append(n + m + 1)
        matching = [-1] * n
        while True:
            flag = False
            q = queue.Queue()
            q.put(0)
            visit = [0 for _ in range(n + m + 2)]
            prev = [[] for _ in range(n + m + 2)]
            while not q.empty():
                s = q.get()
                for x in new_adj[s]:
                    if visit[x] == 0:
                        q.put(x)
                        prev[x].append(s)
                        visit[x] = 1
                    if x == n + m + 1:
                        flag = True
                        break
                if flag == True:
                    break
            if flag == False:
                return matching
            v = n + m + 1
            while v != 0:
                u = prev[v][0]
                new_adj[v].append(u)
                new_adj[u].remove(v)
                if u > 0 and u <= n and v > n and v <= n + m:
                    matching[u - 1] = v - n - 1
                elif v > 0 and v <=n and u > n and u <= n + m:
                    matching[v - 1] = -1                   
                v = u

    def solve(self):
        adj_matrix = self.read_data()
        matching = self.find_matching(adj_matrix)
        self.write_response(matching)

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
