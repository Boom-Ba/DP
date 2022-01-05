#problem: given m by n mat, has value -1, 0,1, can only visited value!=-1
# can go left or down if row is odd
# go right or down if even
# if i&1 denote odd

def isSafe(i,j,m,n,mat):
  return 0<=i<m and 0<=j<n and mat[i][j]!=-1
def MathPathSum(mat):
  m,n =len(mat),len(mat[0])
  dp =mat.copy()
  for i in range(m-2,-1,-1):
    if i&1: #if odd pick max(left,down)
      for j in range(0,n):
        if isSafe(i,j,m,n,mat): #left,down
          left = dp[i][j-1] if isSafe(i,j-1,m,n,mat) else 0
          down =dp[i+1][j] if isSafe(i+1,j,m,n,mat) else 0
          dp[i][j]+=max(left,down)
    else:
      for j in range(n-1,-1,-1):
        if isSafe(i,j,m,n,mat): 
          down =dp[i+1][j] if isSafe(i+1,j,m,n,mat) else 0
          right =dp[i][j+1] if isSafe(i,j+1,m,n,mat) else 0 
          dp[i][j] +=max(right,down)
  return dp
mat =[[1,1,-1,1,1],
      [1,0,0,-1,1],
      [1,1,1,1,-1],
      [-1,-1,1,1,1],
      [1,1,-1,-1,1]]
MathPathSum(mat)
# [[9, 8, -1, 3, 2],
#  [7, 7, 7, -1, 1],
#  [6, 5, 4, 3, -1],
#  [-1, -1, 1, 2, 3],
#  [1, 1, -1, -1, 1]]
