# https://leetcode.com/problems/valid-triangle-number/
# https://www.hellointerview.com/learn/code/two-pointers/valid-triangle-number

def triangleNumber(heights: List[int]):
    heights.sort()
    count = 0

    for i in range(len(heights) - 1, 1, -1):
        left = 0
        right = i - 1

        while left < right:
            if heights[left] + heights[right] > heights[i]:
                count += right - left
                right -= 1
            else:
                left += 1
    
    return count
    
print(triangleNumber(heights=[11,4,9,6,15,18])) # 10
print(triangleNumber(heights=[1,2,3,4])) # 1
print(triangleNumber(heights=[1, 1])) # 0
print(triangleNumber(heights=[1,8,2,10,3,5,12,15,20])) # 14
print(triangleNumber(heights=[3,4,1,2,2,4,1,3,2])) # 39