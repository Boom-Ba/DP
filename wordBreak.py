#recursion
def wordBreak1(word,words):
  if not word:
    return True
  for i in range(1,len(word)):
    prefix=word[:i]
    if prefix in words and wordBreak1(word[i:],words):
      return True
  return False
#memorization
def wordbreak(word,words):
  dp={}
  if word in words:
    return True
  def solve(word,words,dp):
    if word in dp:
      return dp[word]
    for i in range(1,len(word)+1):
      if word[:i] in words:
        dp[word[:i]]=True
        if solve(word[i:],words,dp):
          dp[word[i:]]=True
          return True
      else:
        dp[word[:i]]=False
    # print(dp)
    return False
  return solve(word,words,dp)
#print all res
def wordBreak(words,word,i,output,sols):
  #base
  if i ==len(word):
    sols.append(output)
    return 
  for j in range(i,len(word)):
    prefix=word[i:j+1]
    if prefix in words:
      wordBreak(words,word,j+1,output+' '+prefix,sols)

words = [
        'self', 'th', 'is', 'famous', 'Word', 'break', 'b', 'r',
        'e', 'a', 'k', 'br', 'bre', 'brea', 'ak', 'problem'
    ]
 
    # input string
word = 'Wordbreakproblem'
sols=[]
wordBreak(words,word,0,'',sols)
