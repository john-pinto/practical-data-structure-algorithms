# https://www.hellointerview.com/learn/code/sliding-window/maximum-points-you-can-obtain-from-cards
# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

def maxScore(cards: List[int], k: int):
    total_points = sum(cards)
    if len(cards) == k:
        return total_points

    cur_points = 0
    max_points = 0
    start = 0

    for end in range(len(cards)):
        cur_points += cards[end]

        if end - start + 1 == len(cards) - k:
            max_points = max(max_points, total_points - cur_points)
            cur_points -= cards[start]
            start += 1
    
    return max_points