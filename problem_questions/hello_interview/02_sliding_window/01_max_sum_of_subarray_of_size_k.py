# https://www.hellointerview.com/learn/code/sliding-window/maximum-sum-of-subarrays-of-size-k
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

def maxSum(self, nums: List[int], k: int):
    max_sum = float('-inf')
    curr_sum = 0
    start = 0
    
    for end in range(len(nums)):
        curr_sum += nums[end]
    
        if end - start + 1 == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= nums[start]
            start += 1
    
    return max_sum