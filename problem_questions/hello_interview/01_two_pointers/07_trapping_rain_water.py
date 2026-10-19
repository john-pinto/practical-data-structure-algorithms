# https://leetcode.com/problems/trapping-rain-water/
https://www.hellointerview.com/learn/code/two-pointers/trapping-rain-water


def trappingWater(height: List[int]):
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    count = 0

    while left < right:
        # Checking the container walls for both left and right
        if left_max < right_max:
            left += 1
            if height[left] >= left_max:
                left_max = height[left]
            else:
                # Getting the total count between the difference between current pointer and the max pointer
                count += left_max - height[left]
        else:
            right -= 1
            if height[right] >= right_max:
                right_max = height[right]
            else:
                count += right_max - height[right]

    return count

print(trappingWater(height=[0,1,0,2,1,0,1,3,2,1,2,1]) # 6
print(trappingWater(height=[[4,2,0,3,2,5]]) # 9
print(trappingWater(height=[1,1,1,1,1]) # 0
print(trappingWater(height=[]) # 0
print(trappingWater(height=[4,2,3]) # 1