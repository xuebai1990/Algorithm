# Uses python3
import math

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def MinAndMax(i, j, mi, Ma, op):
    minx = math.inf
    maxx = -math.inf
    for k in range(i, j):
        a = evalt(Ma[i][k], Ma[k + 1][j], op[k])
        b = evalt(Ma[i][k], mi[k + 1][j], op[k])
        c = evalt(mi[i][k], Ma[k + 1][j], op[k])
        d = evalt(mi[i][k], mi[k + 1][j], op[k])
        minx = min(minx, a, b, c, d)
        maxx = max(maxx, a, b, c, d)
    return minx, maxx

def get_maximum_value(dataset):
    #write your code here
    n = len(dataset)
    n = (n - 1) // 2
    num = []
    op = []
    num.append(int(dataset[0]))
    for i in range(0, n):
        num.append(int(dataset[2 * i + 2]))
        op.append(dataset[2 * i + 1])
    n = len(num)
    mi = [[ 0 for i in range(n) ] for j in range(n)]
    Ma = [[ 0 for i in range(n) ] for j in range(n)]
    for i in range(0, n):
        mi[i][i] = num[i]
        Ma[i][i] = num[i]
    for s in range(1, n):
        for i in range(0, n - s):
            j = i + s
            mi[i][j], Ma[i][j] = MinAndMax(i, j, mi, Ma, op)
    return Ma[0][n - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
