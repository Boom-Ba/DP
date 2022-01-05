import sys
#given an array, to find the maximum value of expression A[i]-A[j]+A[k]-A[w] 
#for all i>j>k>w, 
#DP, time: n
def maxValueExpression(arr,n):
  if n<4:
    return -1
  first=[-sys.maxsize]*(n+1)
  for i in range(n-1,-1,-1):
    first[i] =max(arr[i],first[i+1])
  print(first)
  second=[-sys.maxsize]*n
  for i in range(n-2,-1,-1):
    second[i] =max(second[i+1],first[i]-arr[i])
  third =[-sys.maxsize]*(n-1)
  for i in range(n-3,-1,-1):
    third[i] =max(third[i+1],second[i]+arr[i])
  last =[-sys.maxsize]*(n-2)
  for i in range(n-4,-1,-1):
    last[i] =max(last[i+1],third[i]-arr[i])
  return last[0]

