##dp count how many ways match a pattern to a string 
def count(string,pattern):
  dp =[[0 for _ in range(len(pattern)+1)] for _ in range(len(string)+1)]
  for i in range(len(string)+1):
    dp[i][0]=1 #finish pattern string from right to left can get 1 way
  for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
      #if the last character match, current count += the count of excluding the last character in both string and pattern
      #else the current count only includes the count without including the current character
      dp[i][j] =(dp[i-1][j-1] if string[i-1]==pattern[j-1] else 0 )+ dp[i-1][j]
  return dp[len(string)][len(pattern)]
count('subsequence','sue' )

##recursion way 
#count number of times a pattern appears in a given string as subsequence
#string = 'subsequence' pattern ='sue' 
def count(string,pattern,m,n):
  #m =index of string
  if m==0 and n==0: 
    return 1 if string[0]==pattern[0] else 0
  if m<0: #all characters in string has been used 
    return 0 
  if n<0: #pattern string has completely matched, so return 1 solution 
    return 1
  if n>m: #pattern has  more chars than string, it is impossible for getting a solution
    return 0
  return (count(string,pattern,m-1,n-1) if string[m]==pattern[n] else 0 )+ count(string,pattern,m-1,n)
  
  ##variant for another problem to check if pattern can be matched to string 
  #to find if there is a way to match pattern with string
def match(string,pattern,m,n):
  #m =index of string
  if m==0 and n==0: 
    return True if string[0]==pattern[0] else False
  if m<0: #all characters in string has been used 
    return False
  if n<0: #pattern string has completely matched, so return 1 solution 
    return True
  if n>m: #pattern has  more chars than string, it is impossible for getting a solution
    return False
  return (match(string,pattern,m-1,n-1) if string[m]==pattern[n] else False ) or match(string,pattern,m-1,n)
string = 'subsequence' 
pattern ='sae' 
match(string,pattern ,len(string)-1,len(pattern)-1)
