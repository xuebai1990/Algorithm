#!/usr/bin/python3

import sys, threading, math

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

  def IsBinarySearchTree(self,ind,mini,maxi):
  # Implement correct algorithm here
    if self.n == 0:
        return True
    if ind == -1:
        return True
    if self.key[ind] < mini or self.key[ind] > maxi:
        return False
    flag1 = self.IsBinarySearchTree(self.left[ind],mini,self.key[ind]-1)
    flag2 = self.IsBinarySearchTree(self.right[ind],self.key[ind],maxi)
    return flag1 and flag2

def main():
  tr = Tree()
  tr.read()
  x = math.inf
  flag = tr.IsBinarySearchTree(0, -x, x)
  if flag:
    print("CORRECT")
  else:
    print("INCORRECT")

threading.Thread(target=main).start()
