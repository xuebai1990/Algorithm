# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    vw=[]
    for i in range(0,n):
        vw.append(float(values[i])/weights[i])

    for i in range(0,n-1):
        for j in range(n-1,i,-1):
            if vw[j-1]<vw[j]:
#                tmp=vw[j-1]
#                vw[j-1]=vw[j]
#                vw[j]=vw[j-1]
#                tmp=values[j-1]
#                values[j-1]=values[j]
#                values[j]=tmp
#                tmp=weights[j-1]
#                weights[j-1]=weights[j]
#                weights[j]=tmp               
                vw[j-1],vw[j]=vw[j],vw[j-1]
                values[j-1],values[j]=values[j],values[j-1]
                weights[j-1],weights[j]=weights[j],weights[j-1] 

    sw=0.0   
    for i in range(0,n):
        if sw<capacity:
            if (capacity-sw)>=weights[i]:
                sw=sw+weights[i]
                value=value+values[i]
            else:
                frac=(capacity-sw)/weights[i]
                sw=sw+frac*weights[i]
                value=value+frac*values[i]

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
