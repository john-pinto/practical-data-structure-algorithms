# Two Sum
# https://leetcode.com/problems/two-sum/description
# https://www.hellointerview.com/learn/code/two-pointers/two-sum


def twoSum(nums, target):
    output = {}

    for i, num in enumerate(nums):
        if num in output:
            return [output[num], i]
        else:
            output[target - num] = i
            
def twoSum(self, nums: List[int], target: int):
    # Your code goes here
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return True
        
        if total < target:
            left += 1
        else:
            right -= 1
        
    return False


print(twoSum(nums=[2, 7, 11, 15], target=9))
print(twoSum(nums=[3, 2, 4], target=6))
print(twoSum(nums=[3, 3], target=6))
