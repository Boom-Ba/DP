class Solution:
	def findOptimalProduct(self, dims: List[int]) -> int:
		lookup =[[0 for _ in range(len(dims))] for _ in range(len(dims))]
		def solve(dims, l,r):
			res= sys.maxsize
			if r<=l+1:
				return 0
			if lookup[l][r]!=0:
				return lookup[l][r]
			for k in range(l+1,r):
				cost = solve(dims, l, k )
				cost+= solve(dims, k,r)
				cost+= dims[l]*dims[k]*dims[r]
				if cost<res:
					res=cost
			lookup[l][r]=res
			return lookup[l][r]
		return solve(dims,0,len(dims)-1)
