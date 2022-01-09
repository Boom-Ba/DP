#recur + memorization
#i, t - memorization d -look up to record the value(count) of key(#items, target)
def count(target,S,n,lookup):
  key=(n,target)
  if key in lookup:
    return lookup[key]
  if target==0:
    return 1
  if target<0 or n<0:
    return 0

  #exclude nth coin + include nth coin
  lookup[key]= count(target,S,n-1,lookup)+count(target-S[n],S,n,lookup)
  return lookup[key]

  def count(S, target):
  lookup =[[0 for _ in range(target+1)] for _ in range(len(S)+1)]

  #if target==0: we have 1 solution for all # items
  for i in range(len(lookup)):
    lookup[i][0]=1
  
  for i in range(1,len(lookup)):##items can use
    for j in range(1, len(lookup[0])): #target sum to
      if j<S[i-1]: #target less than coin[i]
        lookup[i][j]=lookup[i-1][j] #can't include current item
      if j>=S[i-1]:
        #has enough space/weight to include current item
        #so total #ways is both include and exclude 
        lookup[i][j]=lookup[i][j-S[i-1]]+lookup[i-1][j]
  return lookup[len(S)][target]
