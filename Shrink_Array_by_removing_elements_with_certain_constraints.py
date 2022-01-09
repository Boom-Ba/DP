def shrink(nums, k):
		# Write your code here...
		#[7, 8, 8, 9, 10, 9, 9, 10, 11, 10, 11, 12, 11, 12, 13]
		def solve(nums,s,e,k):
			if s>e:
				return 0
			#skip the first element, not form a triplet 
			res = 1+ solve(nums,s+1,e,k)
	 		#start, i, j form a triplet 
			for i in range(s+1,e):
				for j in range(i+1,e+1):
					if nums[s]+k==nums[i] and nums[i]+k ==nums[j]:
						if not solve(nums, s+1, i-1,k) and not solve(nums,i+1, j-1,k):
							t= solve(nums,j+1,e,k)
							res=min(t,res)
						
			return res
		return solve(nums,0,len(nums)-1,k)
