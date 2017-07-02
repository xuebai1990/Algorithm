# python3
import random
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def siftdown(self, i):
        n = self.num_workers // 2
        j = i
        while j <= n - 1:
            maxid = j
            l = 2 * j + 1
            if l < self.num_workers and self.nft[l] < self.nft[maxid]:
                maxid = l
            r = 2 * j + 2
            if r < self.num_workers and self.nft[r] < self.nft[maxid]:
                maxid = r
            if j == maxid:
                break
            else:
                self.nft[j], self.nft[maxid] = self.nft[maxid], self.nft[j]
                self.ind[j], self.ind[maxid] = self.ind[maxid], self.ind[j]
                j = maxid

    def partition2(self, a, b, l, r):
        x = a[l]
        j = l
        for i in range(l + 1, r + 1):
            if a[i] <= x:
                j += 1
                a[i], a[j] = a[j], a[i]
                b[i], b[j] = b[j], b[i]
        a[l], a[j] = a[j], a[l]
        b[l], b[j] = b[j], b[l]
        return j

    def randomized_quick_sort(self, a, b, l, r):
        if l >= r:
            return
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        b[l], b[k] = b[k], b[l]
        m = self.partition2(a, b, l, r)
        self.randomized_quick_sort(a, b, l, m);
        self.randomized_quick_sort(a, b, m + 1, r);

    def find_free_node(self, i, key):
        child1 = 2 * i + 1
        child2 = 2 * i + 2
        if child1 < self.num_workers and self.nft[child1] == key:
            self.fn.append(self.ind[child1])
            self.fi.append(child1)
            self.find_free_node(child1, key)
        if child2 < self.num_workers and self.nft[child2] == key:
            self.fn.append(self.ind[child2])
            self.fi.append(child2)
            self.find_free_node(child2, key) 

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
          self.fn = []
          self.fi = []
          key = self.nft[0]
          self.fn.append(self.ind[0])
          self.fi.append(0)
          self.find_free_node(0, key)
          arrayfn = self.fn
          arrayfi = self.fi
          self.randomized_quick_sort(arrayfn, arrayfi, 0, len(arrayfn) - 1)
          for j in range(len(arrayfn)):
            self.assigned_workers[i] = arrayfn[j]
            self.start_times[i] = self.nft[arrayfi[j]]
            self.nft[arrayfi[j]] = self.nft[arrayfi[j]] + self.jobs[i]
            i = i + 1
          self.randomized_quick_sort(arrayfi, arrayfi, 0, len(arrayfi) - 1)
          for j in range(len(arrayfi) - 1, -1, -1):
            self.siftdown(arrayfi[j])

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()


if __name__ == '__main__':
    job_queue = JobQueue()
    threading.Thread(target=job_queue.solve).start()

