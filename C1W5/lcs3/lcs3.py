#Uses python3

import sys

def lcs3(a, b, c):
    #write your code here
    n = len(a)
    m = len(b)
    l = len(c)
    s = [[[ 0 for i in range(l+1) ] for j in range(m+1) ] for k in range(n+1) ]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                if a[i - 1] == b[j - 1] and b[j - 1] == c[k - 1]:
                    s[i][j][k] = s[i - 1][j - 1][k - 1] + 1
                else:
                    x = s[i - 1][j][k]
                    y = s[i][j - 1][k]
                    z = s[i][j][k - 1]
                    u = s[i - 1][j - 1][k]
                    v = s[i - 1][j][k - 1]
                    w = s[i][j - 1][k - 1]
                    s[i][j][k] = max(x, y, z, u, v, w)
    return s[n][m][l]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
