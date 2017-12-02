# python3
from sys import stdin
from time import time
import numpy as np

epsilon=1e-9
  
def allocate_ads(n, m, A, b, c):  
  # Write your code here
  Big = 1e7
  z = []
  solu = [0 for _ in range(m)]
  basic = []
  for i in range(m):
      z.append(-c[i])
  lt = []
  af = []
  count = m
  for i in range(n):
      if b[i] < -epsilon:
          b[i] = -b[i]
          for j in range(len(A[i])):
              A[i][j] = -A[i][j]
          lt.append(i)
          z.append(0)
          z.append(Big)
          solu.append(0)
          solu.append(b[i])
          basic.append(count+1)
          af.append(count+1)
          count += 2
          for j in range(n):
              if i == j:
                  A[j].append(-1)
                  A[j].append(1)
              else:
                  A[j].append(0)
                  A[j].append(0)
      else:
          z.append(0)
          solu.append(b[i])
          basic.append(count)
          count += 1
          for j in range(n):
              if i == j:
                  A[j].append(1)
              else:
                  A[j].append(0)
  AA = np.array(A,dtype='float64')
  zz = np.reshape(np.array(z,dtype='float64'), (1,AA.shape[1]))
  b.append(0)
  bb = np.reshape(np.array(b,dtype='float64'), (AA.shape[0]+1,1))
  AA = np.concatenate((AA,zz),axis=0)
  AA = np.concatenate((AA,bb),axis=1)
  for i in lt:
      scale = Big
      AA[n] = AA[n] - AA[i] * scale
  while any(AA[n,0:(AA.shape[1]-1)] < -epsilon):
      piv_element = np.argmin(AA[n, 0:(AA.shape[1]-1)])
      index = -1
      rmin = 1e9
      for i in range(n):
          if AA[i][piv_element] > epsilon:
              r = AA[i,AA.shape[1]-1]/AA[i][piv_element]
              if r < rmin:
                  rmin = r
                  index = i
      if index == -1:
          return (1, [0] * m)
      scale = AA[index,piv_element]
      AA[index] = AA[index] / scale
      tpa = np.reshape(AA[index], (1, AA.shape[1]))
      tpb = np.reshape(AA[:,piv_element], (AA.shape[0], 1))
#      for i in range(AA.shape[0]):
#          if i == index or abs(AA[i,piv_element]) < epsilon:
#              continue
#          else:
#              scale = AA[i,piv_element]
#              AA[i] = AA[i] - AA[index] * scale
      AA = AA - np.matmul(tpb, tpa)
      AA[index] = tpa
      solu[piv_element] = AA[index,AA.shape[1]-1]
      solu[basic[index]] = 0
      basic[index] = piv_element
  for i in range(n):
      solu[basic[i]] = AA[i,AA.shape[1]-1]
  if any(solu[i] < -epsilon for i in range(AA.shape[1]-1)) or (len(af) > 0 and any(solu[i] > epsilon for i in af)):
      return (-1, solu[0:m])
  return (0, solu[0:m])


n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = allocate_ads(n, m, A, b, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")

