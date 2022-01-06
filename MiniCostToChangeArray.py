##problem: we have an array A, we want to change it
## to a new array A_new, such that each element has difference
## t, what would be the minimal changes?
## ex : 1303 -> change to 2323 with different =1, we need 3 adjustments
#       1+0+2+0 = 3 changes
#A=[1,3,0,3], diff=1 
import sys
def minOperations(A, diff): 

  M =max(A)+1
  #row: items, col: target_value
  dp = [[sys.maxsize for _ in range(M+1)] for _ in range(len(A))]
  #with 0 item, it will be 0 ways to get target
  for i in range(len(A)): #item#
    for j in range(M+1): #target-value
      if i==0: #first row, with only 1 element
              #cost is the abs(target-A[i]) 
        dp[i][j] =abs(j-A[i])
      else:
        for k in range( max(j-diff,0), min(j+diff+1,M+1)):
          #pick the minimum number operations for getting prev element + the current num operations
          dp[i][j] =min(dp[i][j],dp[i-1][k]+abs(A[i]-j))
  
  return min(dp[-1])

A=[1,3,0,3]
diff=1 
minOperations(A, diff)
#   0  1   2  3  4
# [[1, 0, 1, 2, 3], 
#  [3, 2, 1, 1, 3], 
#  [2, 2, 3, 4, 5], 
#  [5, 4, 3, 3, 5]]
