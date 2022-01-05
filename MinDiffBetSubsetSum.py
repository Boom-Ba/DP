import sys
from IPython.core.display import display_jpeg
"""
[10,20,15,5,25]

sum =75 
75//2 = 37 

2 states: s1,sum(sum of whole set=75)
lookup table: represents with all items, can we sum to a taget value 
in the subset sum problem, we calculate all possible ways for 0 to 75
    0 1 2 3 4 5 6 7 8 9 10..75
 0  T
 1  T                    T
 2  T
 3  T
 4  T
 5  T         T         T
"""
#use knapsack solve min subset difference
def knapsack(S):
  sum_=sum(S) #75
  dp =[[False for _ in range(sum_+1)] for _ in range(len(S)+1)]
  m,n=len(dp),len(dp[0])
  for i in range(m):
    dp[i][0]=True
  for i in range(1,m):
    for j in range(1,n):
      #if possible to use i #number of items to sum to j
      if j<S[i-1]: #if sum < curr item's value, cann't include item
        dp[i][j]=dp[i-1][j]
      if j>=S[i-1]:
        dp[i][j]=dp[i-1][j-S[i-1]] or dp[i-1][j]
  return dp
S=[10,20,15,5,25]
sum_=sum(S)
dp=knapsack(S)
minDiff= sys.maxsize
#Sum of subset1 at most sum to half, for deduplication
for i in range(1,sum_//2+1):
  #dp last row represents if we can use all of items, possible sum  we can get
  if dp[-1][i]==True:
    s2=sum_-i
    minDiff=min(minDiff,abs(s2-i))
minDiff
###################################################
##recursion
#exponential time and occupied call stack space 
def minDiff(sum1,sum2,n,S):
  #base case 0 left, calculate the Sum difference
  if n<0:
    return abs(sum1-sum2)
  #include the current in s1, and do recursion on remaining n-1
  include =minDiff(sum1+S[n],sum2,n-1,S)
  exclude= minDiff(sum1,sum2+S[n],n-1,S)
  return min(include,exclude)

S=[10,20,15,5,25]
#i s1 s2 s1 s2 s1       
minDiff(0,0,len(S)-1,S)
