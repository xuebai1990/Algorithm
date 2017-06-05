# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    result = 0
    n = len(w)
    wei = [ [ 0 for i in range(n + 1) ] for j in range(W + 1) ]
#    for i in range(W + 1):
#        wei[i][0] = 0
#    for i in range(n + 1):
#        wei[0][i] = 0
    for x in range(1, n + 1):
        for y in range(1, W + 1):
            wei[y][x] = wei[y][x - 1]
            if w[x - 1] <= y:
                val = wei[y - w[x - 1]][x - 1] + w[x - 1]
                if val > wei[y][x]:
                    wei[y][x] = val

    return wei[W][n]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
