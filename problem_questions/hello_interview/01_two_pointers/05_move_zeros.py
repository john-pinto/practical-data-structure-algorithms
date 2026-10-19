# https://leetcode.com/problems/move-zeroes/
# https://www.hellointerview.com/learn/code/two-pointers/move-zeroes

def moveZeroes(self, nums: List[int]):
    zero_index = 0

    for i in range(len(nums)):
        # Looking for non zero number and swaping with first zero index
        if nums[i] != 0:
            nums[i], nums[zero_index] = nums[zero_index], nums[i]
            
            # Possible that the zero number index is the next index
            zero_index += 1
    
    return nums


print(moveZeroes(nums=[1,0,4,0,3,0,1])) # [1,4,3,1,0,0,0]
print(moveZeroes(nums=[0,0,1])) # [1,0,0]
print(moveZeroes(nums=[1,2,3])) # [1,2,3]
print(moveZeroes(nums=[0,0,0])) # [0,0,0]