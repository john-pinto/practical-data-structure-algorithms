# 3Sum
# https://leetcode.com/problems/3sum/description/
# https://www.hellointerview.com/learn/code/two-pointers/3-sum


def threeSum(self, nums: List[int]):
    # Sorting the list
    nums.sort()
    result = []

    # Range to be less by two index for left and right pointers to not move beyond the list
    for i in range(len(nums) - 2):
        # If duplicate as previous then continue
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Checking duplicates for both left and right pointers and moving if found
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1

    return result


print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
print(threeSum(nums=[0, 1, 1]))
print(threeSum(nums=[0, 0, 0]))
