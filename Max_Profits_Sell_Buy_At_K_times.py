#get max profit if allow k times transactions, k=3
#dp[i][j] represents the max profits can make at ith transaction at jth day
prices=[1, 5, 2, 3, 7, 6, 4, 5]
def max_profit(prices,k):
  dp =[[0 for _ in range(len(prices))] for _ in range(k+1)]
  #at row 0, all profits are 0 when there is no transaction
  for i in range(1,len(dp)): #i -th transaction 
    for j in range(len(dp[0])): #j day
      #calculate max profit of no transaction at j day or having one transaction
      dp[i][j] =max(dp[i][j],dp[i][j-1])
      for k in range(j):
        dp[i][j]= max(dp[i][j], prices[j] -prices[k] + dp[i-1][k]) 
  return dp
max_profit(prices,3)
##get maxi profits, sell stock with any numbers 
a=[1,5,2,3,7,6,4,5]
def sell_stock_k_times(a):
  res=[]
  local_min=a[0]
  profit=0
  for i in range(1,len(a)):
    if a[i-1]>a[i]:
      local_min =a[i]
    #sell at peak a[i-1]<=a[i]>a[i+1]
    if a[i-1]<=a[i] and i+1<len(a) and a[i]>a[i+1] or i==len(a)-1:
      profit += a[i]-local_min
sell_stock_k_times(a)
import sys
##basic algorithm is to
##find the max difference (once) between 2 elements in array
def max_diff(A):
  maxi =A[-1]
  diff=-sys.maxsize
  for i in range(len(A)-2,-1,-1):
    if A[i] > maxi:
      maxi =A[i]
    else:
      diff =max(diff,maxi-A[i])
  return diff
max_diff(arr)
arr= [2,7,9,5,1,3,5]
    
