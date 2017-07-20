# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
  def read(self):
    self.n = int(sys.stdin.readline())
    self.key = [0 for i in range(self.n)]
    self.left = [0 for i in range(self.n)]
    self.right = [0 for i in range(self.n)]
    for i in range(self.n):
      [a, b, c] = map(int, sys.stdin.readline().split())
      self.key[i] = a
      self.left[i] = b
      self.right[i] = c

  def inOrder(self,ind,result):
    # Finish the implementation
    # You may need to add a new recursive method to do that
    if ind == -1:
        return
    self.inOrder(self.left[ind],result)
    result.append(self.key[ind])
    self.inOrder(self.right[ind],result)

  def preOrder(self,ind,result):
    if ind == -1:
        return
    result.append(self.key[ind])
    self.preOrder(self.left[ind],result)
    self.preOrder(self.right[ind],result)
    
    # Finish the implementation
    # You may need to add a new recursive method to do that

  def postOrder(self,ind,result):
    if ind == -1:
        return
    self.postOrder(self.left[ind],result)
    self.postOrder(self.right[ind],result)
    result.append(self.key[ind])
    # Finish the implementation
    # You may need to add a new recursive method to do that

def main():
	tree = TreeOrders()
	tree.read()
	result1 = []
	result2 = []
	result3 = []
	tree.inOrder(0, result1)
	tree.preOrder(0, result2)
	tree.postOrder(0, result3)
	print(" ".join(str(x) for x in result1))
	print(" ".join(str(x) for x in result2))
	print(" ".join(str(x) for x in result3))

threading.Thread(target=main).start()
