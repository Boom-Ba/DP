#variant of Minimum Edit distance
def kPalindrome(s, k):
  #check if s ='abcdba' k=1 use one remove can make it to palindrome
  lookup={}
  def min_distance(s,reversed_s,m,n,lookup):
    #return min deletion needs to make s equals reversed_s
    key= (m,n)
    if key in lookup:
      return lookup [key]
    if m==0:
      return n
    if n==0:
      return m
    if s[m-1]==reversed_s[n-1]:
      lookup[key] =min_distance(s,reversed_s,m-1,n-1,lookup)
      return lookup[key]
    lookup[key]= min(min_distance(s,reversed_s,m-1,n,lookup),min_distance(s,reversed_s,m,n-1,lookup))+1
    return lookup[key]
  reversed_s=s[::-1]
  o =min_distance(s,reversed_s,len(s),len(s),lookup)
  return o//2
kPalindrome('abcdba', 1)
# Function to check if the given string is k–palindrome or not
def isKPalindrome(X, K):
    #number of deletes make string to be palindrome
    # 'Y' is a reverse of 'X'
    Y = X[::-1]
 
    n = len(X)
 
    # lookup table to store solution of already computed subproblems
    T = [[0 for x in range(n + 1)] for y in range((n + 1))]
 
    # fill the lookup table `T[][]` in a bottom-up manner
    for i in range(n + 1):
        for j in range(n + 1):
            #if etither is empty, will need to remove all chars
            if i == 0 or j == 0:
                T[i][j] = i + j
            if X[i-1]==Y[j-1]:
               T[i][j]=T[i-1][j-1]
            else:
              T[i][j]= min(T[i-1][j],T[i][j-1])+1
    return T[-1][-1] 
isKPalindrome('cabcbc', 1)
#third solution is to find the Longest Palindrome String, then minus the LPS
#which is the number of remove needs
import sys
def findMaxLengthPalindrome(s):
  def solve(s,l,r):
    if l>r:
      return 0
    if l==r:
      return 1
    if s[l]==s[r]:
      return solve(s,l+1,r-1)+2 
    return max(solve(s,l+1,r),
               solve(s,l,r-1))
  l=len(s)
  l,r =0,l-1
  maxlen =-sys.maxsize
  maxlen=solve(s,l,r)
  return maxlen if maxlen!=-sys.maxsize else maxlen

ss='CABCB'
findMaxLengthPalindrome(ss)  
