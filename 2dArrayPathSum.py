import sys
def calculateMinPathSum(mat):
  m,n=len(mat),len(mat[0])
  dp =mat.copy()
  for i in range(len(dp)-2,-1,-1):
    j=0
    while j<n:
      left=dp[i+1][j-1] if j>=0 else sys.maxsize
      middle =dp[i+1][j] 
      right =dp[i+1][j+1] if j+1<n else sys.maxsize
      dp[i][j] +=min(left,middle,right)
      j+=1
  return dp
def calculateMaxPathSum(mat):
  m,n=len(mat),len(mat[0])
  dp =mat.copy()
  for i in range(len(dp)-2,-1,-1):
    j=0
    while j<n:
      left=dp[i+1][j-1] if j-1>=0 else 0
      middle =dp[i+1][j] 
      right =dp[i+1][j+1] if j+1<n else 0
      dp[i][j] +=max(left,middle,right)
      j+=1
  return dp
mat= [
      [5,1,2,6],
      [9,9,7,5],
      [3,1,4,8]
      ]
"""
dp last row =[3,1,4,8]
dp from len(dp-2) to first row
dp[i][j]+=min(dp[i+1][j],dp[i+1][j-1],dp[i+1][j+1])
"""
calculateMaxPathSum(mat)
