
#You are given an integer array nums and an integer x. In one operation, 
#you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
#Note that this modifies the array for future operations.
#Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.

# Example 1:
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

#since by removing element to decrease x to -> 0, it equals find the subarray sum to target sum(array)-x
def minOperations(self, nums: List[int], x: int) -> int:  
        n_sum =sum(nums)
        if n_sum<x:
            return -1
        if n_sum ==x:
            return len(nums)
        subarray_sum =n_sum-x
        
        curr_sum =0
        left=0
        maxlen =0
        for right, val in enumerate(nums):
            curr_sum +=val
            
            while curr_sum>subarray_sum:
                curr_sum -= nums[left]
                left+=1
            if curr_sum ==subarray_sum:
                maxlen =max(maxlen, right-left+1)
        return len(nums)-maxlen if maxlen>0 else -1
        
