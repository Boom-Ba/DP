##problem is to find all valid triplets such that, the sum of
##two elements is the third value
# A=[1,2,3,4,5]
# The valid triplets are:
# (1, 2, 3), (1, 3, 4), (1, 4, 5), (2, 3, 5)
def count(A,n):
  max_val =max(A)
  freq =[0 for i in range(max_val+1)]
  
  for i in range(n):
    freq[A[i]]+=1
  print(freq)
  ans= 0

  ##case1: 0 0 0 freq[0] chose 3 = (freq[0])!/3!*(freq[0]-3)!
  ans+= freq[0]*(freq[0]-1)*(freq[0]-2)//6 

  #case2: x+x =2x
  for i in range(1, max_val // 2+1):
    ans += (freq[i] *
      (freq[i] - 1) // 2 * freq[2 * i])
 

  #case3: 0+x=x freq[i] choose 2
  for i in range(1,max_val+1):
    ans +=freq[0] * (freq[i]*freq[i-1])//2

  #case4: x+y =x+y
  for x in range(1,max_val+1):
    for y in range(x+1,max_val-x+1):
      ans +=freq[x]*freq[y]*freq[x+y]
  return ans

            
count([1,2,3,4,5],5)
