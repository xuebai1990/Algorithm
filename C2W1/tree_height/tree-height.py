# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self):
        self.child = []

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.nd = []
                for i in range(self.n):
                    x = Node()
                    self.nd.append(x)
                for i in range(self.n):
                    if self.parent[i] == -1:
                        self.root = i
                    else:
                        self.nd[self.parent[i]].child.append(i) 

        def compute_height(self, num):
                # Replace this code with a faster implementation
                if len(self.nd[num].child) == 0:
                    return 1
                else:
                    a = []
                    for i in range(len(self.nd[num].child)):
                        a.append(1+self.compute_height(self.nd[num].child[i]))
                    return max(a)

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height(tree.root))

#main()
threading.Thread(target=main).start()
