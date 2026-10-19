# https://leetcode.com/problems/sort-colors/
# https://www.hellointerview.com/learn/code/two-pointers/sort-colors

def sortColors(nums: List[int]):
    left, right = 0, len(nums) - 1
    i = 0

    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1
    
    return nums
    

print(sortColors(nums=[2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(sortColors(nums=[2,2,1])) # [1,2,2]
print(sortColors(nums=[0])) # [0]
print(sortColors(nums=[1,2,0])) # [0,1,2]
print(sortColors(nums=[2,1,2,0,1,2,2,0])) # [0,0,1,1,2,2,2,2]