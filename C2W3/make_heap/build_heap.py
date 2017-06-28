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
    n = len(self._data) // 2
    for i in range(n - 1, -1, -1):
      j = i
      while j <= n - 1:
        x = min(self._data[j], self._data[2 * j + 1], self._data[2 * j + 2])
        if x == self._data[2 * j + 1]:
          self._swaps.append((j, 2 * j + 1))
          self._data[j], self._data[2 * j + 1] = self._data[2 * j + 1], self._data[j]
          j = 2 * j + 1
        elif x == self._data[2 * j + 2]:
          self._swaps.append((j, 2 * j + 2))
          self._data[j], self._data[2 * j + 2] = self._data[2 * j + 2], self._data[j]
          j = 2 * j + 2
        else: 
          break

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
