# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if segments[j-1].end>segments[j].end:
                segments[j-1],segments[j]=segments[j],segments[j-1]

    #write your code here
    i=0
    while i<n:
        a=segments[i].end
        points.append(a)
        while i<n and a>=segments[i].start:
            i=i+1

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
