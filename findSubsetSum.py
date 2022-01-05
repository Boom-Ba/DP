#dp, time: m*n
def findSubsetSum(a,t):
  sum_=sum(a) #7
  dp =[[False for i in range(sum_+1)] for j in range(len(a)+1)]
  #empty subset makes to True
  for i in range(len(dp)):
    dp[i][0]=True
  for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
      if j<a[i-1]:
        dp[i][j]=dp[i-1][j]
      if j>=a[i-1]: #curr calculating sum>=a[i-1]
        dp[i][j] =dp[i-1][j] or dp[i-1][j-a[i-1]]
  return dp[len(a)][t]

#recursion:exponential
def findSumset(a, i, target, n ):
  if i==n:
    if target==0:
      return True
    return False
  if target<0:
    return False
  return findSumset(a, i+1, target-a[i], n) or findSumset(a, i+1,target,n)
