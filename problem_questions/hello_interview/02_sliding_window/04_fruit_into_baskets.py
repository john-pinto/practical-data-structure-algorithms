# https://leetcode.com/problems/fruit-into-baskets/
# https://www.hellointerview.com/learn/code/sliding-window/variable-length

def totalFruit(fruits: List[int]) -> int:
    max_count = 0
    start = 0
    state = {}

    for end in range(len(fruits)):
        state[fruits[end]] = state.get(fruits[end], 0) + 1

        while len(state) > 2:
            state[fruits[start]] -= 1

            if state[fruits[start]] == 0:
                del state[fruits[start]]
            
            start += 1
        
        max_count = max(max_count, end - start + 1)
    
    return max_count