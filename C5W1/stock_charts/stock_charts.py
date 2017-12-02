# python3
import queue

class StockCharts:
    def read_data(self):
        n, k = map(int, input().split())
        stock_data = [list(map(int, input().split())) for i in range(n)]
        return stock_data

    def write_response(self, result):
        print(result)

    def min_charts(self, stock_data):
        # Replace this incorrect greedy algorithm with an
        # algorithm that correctly finds the minimum number
        # of charts on which we can put all the stock data
        # without intersections of graphs on one chart.
        n = len(stock_data)
        k = len(stock_data[0])
        charts = n
        adj = [[] for _ in range(2 * n + 2)]
        for i in range(n):
            adj[0].append(i + 1)
            for j in range(n):
                if all([x < y for x, y in zip(stock_data[i], stock_data[j])]):
                    adj[i + 1].append(j + n + 1)
        for i in range(n):
            adj[i + n + 1].append(2 * n + 1)
        while True:
            q = queue.Queue()
            q.put(0)
            flag = False
            visit = [0 for _ in range(2 * n + 2)]
            prev = [[] for _ in range(2 * n + 2)]
            while not q.empty():
                s = q.get()
                for x in adj[s]:
                    if visit[x] == 0:
                        q.put(x)
                        visit[x] = 1
                        prev[x].append(s)
                    if x == 2 * n + 1:
                        flag = True
                        break
                if flag == True:
                    break
            if flag == False:
                return charts
            v = 2 * n + 1
            while v != 0:
                u = prev[v][0]
                adj[v].append(u)
                adj[u].remove(v) 
                if u > 0 and u <= n and v > n and v <= 2 * n:
                    charts -= 1
                elif v > 0 and v <= n and u > n and u <= 2 * n:
                    charts += 1
                v = u

    def solve(self):
        stock_data = self.read_data()
        result = self.min_charts(stock_data)
        self.write_response(result)

if __name__ == '__main__':
    stock_charts = StockCharts()
    stock_charts.solve()
