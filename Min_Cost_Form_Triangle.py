import math
import sys
def dist(p1,p2):
  return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1]) *(p1[1]-p2[1]) )
def minWeightTriangle(vertices, i,j):
  cost= sys.maxsize
  if lookup[i][j]!=0.0:
    return lookup[i][j]
  #must has at least three vertices to form a triangle 
  if j<i+2:
    return 0
  for k in range(i+1,j):
    t = dist(vertices[i],vertices[j]) +dist(vertices[k],vertices[j])+dist(vertices[i],vertices[k])
    t+= minWeightTriangle(vertices, i,k)
    t+= minWeightTriangle(vertices, k,j)
    if t<cost:
      cost= t
  lookup[i][j] =cost if cost<sys.maxsize else 0.0
  return lookup[i][j]
if __name__ =='__main__':
  vertices =[[0, 0], [2, 0], [2, 1], [1, 2], [0,1]]
  # vertices =[[1, 2], [0,1]]
  lookup =[[0.0 for _ in range(len(vertices))] for _ in range(len(vertices))]
  res=minWeightTriangle(vertices, 0,len(vertices)-1)
  
  ##dp ->optimized
  import math
import sys
def dist(p1,p2):
  return math.sqrt((p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1]) *(p1[1]-p2[1]) )
def minWeightTriangle(vertices, i,j):
  cost= sys.maxsize
  if lookup[i][j]!=0.0:
    return lookup[i][j]
  #must has at least three vertices to form a triangle 
  if j<i+2:
    return 0
  for dia in range(len(vertices)):
    i =0 
    #only traverse the top right triangle in lookup table 
    for j in range(dia,len(vertices)):
      if i>=len(vertices)-2:
        break
      #must be three verticies and more to form triangle
      if j>=i+2:
        for k in range(i+1,j):
          t = dist(vertices[i],vertices[j]) +dist(vertices[k],vertices[j])+dist(vertices[i],vertices[k])
          t+= lookup[i][k]
          t+= lookup[k][j]
          if t<cost:
            cost= t
      lookup[i][j] =cost if cost<sys.maxsize else 0.0
      i+=1
  return lookup[i][j]
if __name__ =='__main__':
  vertices =[[0, 0], [2, 0], [2, 1], [1, 2], [0,1]]
  # vertices =[[1, 2], [0,1]]
  lookup =[[0.0 for _ in range(len(vertices))] for _ in range(len(vertices))]
  res=minWeightTriangle(vertices, 0,len(vertices)-1)

