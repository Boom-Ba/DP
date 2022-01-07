#Pots of Gold Game Problem using Dynamic Programming
#player1, and oppnent can only choose the first element, last element in an array
#player1 has the choice to pick first
def maxCoinsEarn(A):
  lookup={}
  def solve(A,l,r,lookup):
    key=(l,r)
    if key in lookup:
      return lookup[key]
    if l==r:
      lookup[key]= A[l]
      return lookup[key]
    if  l==r-1:
      lookup[key]= max(A[l],A[r])
      return lookup[key]
    #if player choose left, opponent (left+1,right)
    # value player1 at least can get is A[l] + min(next_choice)
    player_choose_left= A[l] + min(solve(A,l+2,r,lookup), solve(A,l+1,r-1,lookup))
    #opponent: left,right-1, has option {left,right-1}
    player_choose_right= A[r] + min(solve(A,l,r-2,lookup), solve(A,l+1,r-1,lookup))
    lookup[key]=max(player_choose_left,player_choose_right)
    return lookup[key]
  
  return solve(A,0,len(A)-1,lookup)

