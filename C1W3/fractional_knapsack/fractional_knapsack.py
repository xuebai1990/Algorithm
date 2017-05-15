# Uses python3
import sys

def cparray(b,d,f,iBegin,iEnd,a,c,e):
    for k in range(iBegin,iEnd):
        a[k]=b[k]
        c[k]=d[k]
        e[k]=f[k]   

def merge(a,c,e,iBegin,iMiddle,iEnd,b,d,f):
    i0=iBegin
    i1=iMiddle
    for j in range(iBegin,iEnd):
        print i0
        if i0<iMiddle and (i1>=iEnd or a[i0]>=a[i1]):
            b[j]=a[i0]
            d[j]=c[i0]
            f[j]=e[i0]
            i0=i0+1
        else:
            b[j]=a[i1]
            d[j]=c[i1]
            f[j]=e[i1]
            i1=i1+1
#        print b[j]

def splitmerge(a,c,e,iBegin,iEnd,b,d,f):
    if iEnd-iBegin<2:
        return
    iMiddle=(iBegin+iEnd)/2
    splitmerge(a,c,e,iBegin,iMiddle,b,d,f)
    splitmerge(a,c,e,iMiddle,iEnd,b,d,f)
    merge(a,c,e,iBegin,iMiddle,iEnd,b,d,f)
    cparray(b,d,f,iBegin,iEnd,a,c,e)

def get_optimal_value(capacity, weights, values):
    value = 0.
    vw=[]
    for i in range(0,n):
        vw.append(float(values[i])/weights[i])
#    print vw
    vwS=vw
    weightsS=weights
    valuesS=values
    splitmerge(vw,weights,values,0,n,vwS,weightsS,valuesS)
#    print vw,weights,values
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
