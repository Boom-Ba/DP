##find optimal cost to construct BST
##cost frequency list freq[] = { 25, 10, 20 }
##if tree is like:
# 0 -level1 *25
# \
#   2 level2*20
# /
# 1 level3*20
#cost is min(25+40+60)
freq = [25, 10, 20]
def constructBST(frequency):
  def solve(freq, l ,r,level):
    if l>r:
      return 0
    optimalCost = sys.maxsize
    #root could be 0, 1, 2, C（2n,n)/(n+1) = 5 possible ways 
    for root in range(l,r+1):
      leftOptimalCost= solve(freq, l ,root-1,level+1)
      rightOptimalCost=solve(freq,root+1,r,level+1)
    optimalCost = min(optimalCost, freq[root] * level + leftOptimalCost
                                        + rightOptimalCost)
  return solve(frequency, 0 ,len(frequency)-1,1)
