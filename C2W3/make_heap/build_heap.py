# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    m = len(self._data)
    n = m // 2
    for i in range(n - 1, -1, -1):
      j = i
      while j <= n - 1:
        maxid = j
        l = 2 * j + 1
        if l < m and self._data[l] < self._data[maxid]:
          maxid = l
        r = 2 * j + 2 
        if r < m and self._data[r] < self._data[maxid]:
          maxid = r
        if j == maxid:
          break
        else:
          self._swaps.append((j, maxid))
          self._data[j], self._data[maxid] = self._data[maxid], self._data[j]
          j = maxid

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
