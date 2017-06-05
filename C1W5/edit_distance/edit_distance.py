# Uses python3
def edit_distance(s, t):
    #write your code here
    m = len(s)
    n = len(t)
    ed = [[ 0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        ed[i][0] = i
    for i in range(1, n + 1):
        ed[0][i] = i
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                ed[i][j] = ed[i - 1][j - 1]
            else:
                a = ed[i - 1][j] + 1
                b = ed[i][j - 1] + 1
                c = ed[i - 1][j - 1] + 1
                ed[i][j] = min(a, b, c)
    return ed[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
