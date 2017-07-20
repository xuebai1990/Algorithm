#!/usr/bin/python3

import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class Tree:
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

  def IsBinarySearchTree(self,ind,result):
  # Implement correct algorithm here
    if self.n == 0:
        return 1
    if ind == -1:
        return 1
    flag = self.IsBinarySearchTree(self.left[ind],result)
    if flag == 0:
        return 0
    else:
        n = len(result)
        if n != 0:
            if result[n - 1] >= self.key[ind]:
                return 0
        result.append(self.key[ind])
    flag = self.IsBinarySearchTree(self.right[ind],result)
    return flag

def main():
  tr = Tree()
  tr.read()
  result = []
  flag = tr.IsBinarySearchTree(0, result)
  if flag == 1:
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
