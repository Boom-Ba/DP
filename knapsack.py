#knapsack - DP m*n
#knapsack - recursion 2^N
def knapsack(weights,profits,capacity):
  #initially assign -1
  dp= [[ 0 for _ in range(capacity+1)] for _ in range(len(weights)+1)]
  #calculating the current weight
  #if weight ==0 or item==0, simply assign 0
  for i in range(1,len(dp)): 
    # #items can use
    for j in range(1,len(dp[0])): 
      #capacity 
      #if have i-items, the profit can make with weight[j]
      if weights[i-1]>j: #cannot include 
        dp[i][j]=dp[i-1][j]
      if j>=weights[i-1]:
        dp[i][j]= max(dp[i-1][j], dp[i-1][j-weights[i-1]]+profits[i-1])    
  return dp[-1][-1]

def kp_recur(weights, profits, w, n):
  if w <0 or n<0: 
    #base case is not w<0 and n<0, no left weight and no left item can use
    return 0
  if w<weights[n]: #cannot include, 
    return kp_recur(weights, profits, w, n-1)
  if w>=weights[n]:
    return max(kp_recur(weights, profits, w, n-1), kp_recur(weights, profits, w-weights[n], n-1)+profits[n])
    
