##count max length of 1 form to shape +
# example :[010
#          [111]
#          [010]] length =5
import sys
grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]
def count_len (grid):
  m,n=len(grid),len(grid[0])
  left= [[0 for _ in range(n)] for _ in range(m)]
  top= [[0 for _ in range(n)] for _ in range(m)]
  right= [[0 for _ in range(n)] for _ in range(m)]
  bottom= [[0 for _ in range(n)] for _ in range(m)]
  res=-sys.maxsize
  for i in range(m):
    left[i][0] =grid[i][0]
    right[i][n-1]=grid[i][n-1]
    for j in range(n): 
      top[0][j] =grid[0][j]
      bottom[m-1][j]=grid[m-1][j]
      if grid[i][j]==1:
        left[i][j] =left[i][j-1]+1 if 0<=i<m and 0<=j-1<n else grid[i][j]
        top[i][j] =top[i-1][j]+1 if 0<=i-1<m  and 0<=j<n else grid[i][j]
  for i in reversed(range(m)):
    for j in reversed(range(n)): 
      if grid[i][j]==1:
        bottom[i][j]= bottom[i+1][j]+1 if 0<=i+1<m and 0<=j+1<n else grid[i][j]
        right[i][j] = right[i][j+1]+1 if 0<=i<m and 0<=j+1<n else grid[i][j]
  for i in range(m):
    for j in range(n):
      length = min(top[i][j], bottom[i][j], left[i][j], right[i][j])
              # largest `+` would be formed by a cell that has a maximum value
      if length - 1 > res:
          res = length - 1
  return res

def max_ones(grid):
  single_len =count_len(grid)
  return single_len*4+1
max_ones(grid) #17
