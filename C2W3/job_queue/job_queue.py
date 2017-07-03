# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def siftdown(self, i, a, b, n):
        j = i
        nn = n // 2
        while j <= nn - 1:
            maxid = j
            l = 2 * j + 1
            if l < n and a[l] < a[maxid]:
                maxid = l
            r = 2 * j + 2
            if r < n and a[r] < a[maxid]:
                maxid = r
            if j == maxid:
                break
            else:
                a[j], a[maxid] = a[maxid], a[j]
                b[j], b[maxid] = b[maxid], b[j]
                j = maxid

    def heap_sort(self, a, b):
        n = len(a)
        n2 = n // 2
        for i in range(n2 - 1, -1, -1):
            self.siftdown(i, a, b, n)
        nn = n
        for i in range(n - 1):
            a[0], a[nn - 1] = a[nn - 1], a[0]
            b[0], b[nn - 1] = b[nn - 1], b[0]
            nn = nn - 1
            self.siftdown(0, a, b, nn)

    def find_free_node(self, i, key, a, b):
        child1 = 2 * i + 1
        child2 = 2 * i + 2
        if child1 < self.num_workers and self.nft[child1] == key:
            a.append(self.ind[child1])
            b.append(child1)
            self.find_free_node(child1, key, a, b)
        if child2 < self.num_workers and self.nft[child2] == key:
            a.append(self.ind[child2])
            b.append(child2)
            self.find_free_node(child2, key, a, b) 

    def assign_jobs(self):
        # TODO: replace this code with a faster algorithm.
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.nft = [0] * self.num_workers
        self.ind = []
        for i in range(self.num_workers):
          self.ind.append(i)
        i = 0
        while i < len(self.jobs):
          fn = []
          fi = []
          key = self.nft[0]
          fn.append(self.ind[0])
          fi.append(0)
          self.find_free_node(0, key, fn, fi)
          self.heap_sort(fn, fi)
          j = len(fn) - 1
          while j >= 0:
            self.assigned_workers[i] = fn[j]
            self.start_times[i] = self.nft[fi[j]]
            self.nft[fi[j]] = self.nft[fi[j]] + self.jobs[i]
            if self.jobs[i] != 0:
              j -= 1
            i = i + 1
            if i >= len(self.jobs):
              break
          self.heap_sort(fi, fn)
          for j in range(len(fi)):
            self.siftdown(fi[j], self.nft, self.ind, self.num_workers)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

