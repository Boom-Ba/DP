def minDistance(self, word1: str, word2: str) -> int:
      dp={}
      def solve(w1,w2,m,n):
          if m==0:
              return n
          if n==0:
              return m
          key =(m,n)
          if key in dp:
              return dp[key]
          cost = 0 if w1[m-1]==w2[n-1] else 1
          dp[key]= min(solve(w1,w2,m-1,n)+1,
                    solve(w1,w2,m,n-1)+1,
                     solve(w1,w2,m-1,n-1)+cost)
          return dp[key]
      return solve(word1,word2, len(word1),len(word2))
