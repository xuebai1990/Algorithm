# python3
import sys

class Node:
    def __init__(self, start, length, root, color):
        self.next = {}
        self.start = start
        self.length = length
        self.root = root
        self.color = color

def build_suffix_tree(text, color, root):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  l = len(text)
  # Implement this function yourself
  for i in range(0, l):
      current = root
      j = i
      while j < l:
          if text[j] in current.next:
              if current.color != color:
                  current.color = 2
              child = current.next[text[j]]
              st = child.start
              lg = child.length
              k = j + 1
              while k - j < lg and text[k] == text[st + k - j]:
                  k += 1
              if k - j == lg:
                  current = child
                  j = k
              else:
                  oldKey = text[st + k - j]
                  mid = Node(st, k - j, False, color)
                  if current.color != color:
                      mid.color = 2
                  mid.next[text[k]] = Node(k, l - k, False, color)
                  mid.next[oldKey] = child
                  child.start = st + k - j
                  child.length = lg - k + j
                  current.next[text[j]] = mid
          else:
              current.next[text[j]] = Node(j, l - j, False, color)
              if text[j] == "#":
                  current.next[text[j]].color = 1

def dfs(node, p):
    if node.color == 1:
        return p
    elif node.color == 0:
        return node.start + 1
    else:
        x = p
        for value in node.next.values():
            x = min(x, dfs(value, p))
        return x

def solve (p, q):
    result = p
    length = len(p)
    root = Node(0, 0, False, 0)
    build_suffix_tree(p+"#", 0, root)
    build_suffix_tree(q+"$", 1, root)
    for value in root.next.values():
        x = dfs(value, 2*len(p))
        if x - value.start < length:
            length = x - value.start
            result = p[value.start:x]
    return result

p = sys.stdin.readline ().strip ()
q = sys.stdin.readline ().strip ()

ans = solve (p, q)

sys.stdout.write (ans + '\n')
