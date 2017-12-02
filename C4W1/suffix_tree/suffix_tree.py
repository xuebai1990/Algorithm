# python3
import sys
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, start, length, leaf, root):
        self.next = {}
        self.start = start
        self.length = length
        self.leaf = leaf
        self.root = root

def build_suffix_tree(text):
  """
  Build a suffix tree of the string text and return a list
  with all of the labels of its edges (the corresponding 
  substrings of the text) in any order.
  """
  result = []
  ndlist = []
  l = len(text)
  root = Node(None, None, None, True)
  root.next[text[0]] = Node(0, l, 0, False) 
  # Implement this function yourself
  for i in range(1, l):
      current = root
      j = i
      while j < l:
          if text[j] in current.next:
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
                  mid = Node(st, k - j, -1, False)
                  mid.next[text[k]] = Node(k, l - k, i, False)
                  mid.next[oldKey] = child
                  child.start = st + k - j
                  child.length = lg - k + j
                  current.next[text[j]] = mid
          else:
              current.next[text[j]] = Node(j, l - j, i, False)
  print_edge(root, result, text)
  return result

def print_edge(node, result, text):
    if len(node.next) == 0:
        result.append(text[node.start:(node.start+node.length)])
        return
    else:
        for key in node.next:
            print_edge(node.next[key], result, text)
        if not node.root:
            result.append(text[node.start:(node.start+node.length)])        

if __name__ == '__main__':
  text = sys.stdin.readline().strip()
  result = build_suffix_tree(text)
  print("\n".join(result))
