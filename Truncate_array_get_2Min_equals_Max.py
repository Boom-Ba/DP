##problem is to truncate Array, so that the min*2 > max
def findMin(A,l,r):
  if r<l:
    return 0
  subarr = A[l:r+1]
  if 2 * min(subarr) <= max(subarr):
      L = 1 + findMin(A, l + 1, r)
      R = 1 + findMin(A, l, r - 1)
      return min(L, R)
    # we reach here if the array is already balanced
  return 0  
if __name__ =='__main__':
  A=[4, 6, 1, 7, 5, 9, 2]
  res=findMin(A,0,len(A)-1)   
  res  
