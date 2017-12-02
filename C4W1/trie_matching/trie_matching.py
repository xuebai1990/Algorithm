# python3
import sys

def build_trie(patterns):
    tree = dict()
    # write your code here
    count = 1
    for s in patterns:
        current = 0
        for i in range(len(s)):
            t = s[i]
            if not current in tree:
                tree[current] = {}
            if t in tree[current]:
                current = tree[current][t]
            else:
                tree[current][t] = count
                current = count
                count += 1
    return tree

def solve (text, n, patterns):
    result = []
    # write your code here
    tree = build_trie(patterns)
    for i in range(len(text)):
        current = 0
        j = i
        while True:
            if not current in tree:
                result.append(i)
                break
            elif j >= len(text):
                break
            elif text[j] in tree[current]:
                current = tree[current][text[j]]
                j += 1
            else:
                break
    return sorted(result)

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, n, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
