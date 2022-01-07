#Given size of mat, and max k number of turns can make, 
#return total number ways to from top-left to bottom-right
def countWays(M, k):
  T ={} 
  def solve(M,N,i,j,k,isCol):
    if k == -1 or not (0<=i<M and 0<=j<N):
        return 0
    key = (i,j,k)
    if key in T:
      return T[key]
    # If the destination is reached with exactly `k` turns
    if k == 0 and i == M - 1 and j == N - 1:
        T[key] =1
        return T[key]
 
    # If the current direction is along a column
    if isCol:
        # 1. Continue moving along the column
        # 2. Turn right and decrement the number of turns by 1
        T[key]= solve(M, N, i + 1, j, k, isCol) + \
            solve(M, N, i, j + 1, k - 1, not isCol)
        return T[key]
    # If the current direction is along a row
    # 1. Continue moving along the row
    # 2. Turn down and decrement the number of turns by 1
    T[key]= solve(M, N, i, j + 1, k, isCol) + \
        solve(M, N, i + 1, j, k - 1, not isCol)
    return T[key]
  #initially moving along col or row
  i=j=0
  return solve(M,M,i+1,j,k,True)+solve(M,M,i,j+1,k,False)
countWays(3, 1)
