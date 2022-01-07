##problem is to find the min cuts that changes a string to set of palindromes
##hint: 'ABA' is already a palindrome, so no need to cut
##'A' single char is palindrome, so the range of cuts could be [0,len(s)-1]
def isPalindrom(s, l,r):
  while l<r:
    if s[l]!=s[r]:
      return False
    l+=1
    r-=1
  return True 

def find_min_cuts(s):
  #create palindrome mark table
  dp =[[False for _ in range(len(s))] for _ in range(len(s))]
  for i in range(len(s)):
    dp[i][i]=True
    left =i 
    window_size=2
    while window_size<len(s):
      for right in range(left+1,len(s)):
        if s[left]==s[right] and isPalindrom(s,left+1,right-1):
          dp[left][right]= True
      window_size+=1
  print(dp)
  #create min_cuts array to store the minimal number cuts needed
  cuts =[len(s)] *len(s)
  for i in range(len(s)):
    if dp[0][i]==True:
      cuts[i] =0
    t =cuts[i]
    for j in range(i):
      #if cut one more at j
      if cuts[j]+1 < t and dp[j+1][i]==True:
        t =cuts[j]+1
    cuts[i]=t
  return cuts 
#s='banana'
# [[True, False, False, False, False, False], 
#  [False, True, False, True, False, True], 
#  [False, False, True, False, True, False], 
#  [False, False, False, True, False, True], 
#  [False, False, False, False, True, False], 
#  [False, False, False, False, False, True]]
