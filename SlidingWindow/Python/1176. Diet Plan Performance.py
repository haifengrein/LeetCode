#
# @lc app=leetcode.cn id=1176 lang=python3
#
# [1176] 健身计划评估
#

# @lc code=start
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        def evaluate(total):
            if total < lower:
                return -1
            elif total > upper:
                return 1
            return 0
        
        n = len(calories)
        if n < k:
            return 0
        
        points =0
        curr_sum = sum(calories[:k])
        points = evaluate(curr_sum)

        for right in range(k,n):
            curr_sum  = curr_sum  + calories[right] - calories[right - k]
            points += evaluate(curr_sum )
        
        return points
        
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        T_sum = points = 0
        left = 0
        n = len(calories)
        if n < k:
            return 0
        for right in range(n):
            T_sum += calories[right]

            if right - left + 1 == k:
                if T_sum > upper:
                    points += 1
                elif T_sum < lower:
                    points -= 1
                T_sum -= calories[left]
                left += 1
        return points

            
# @lc code=end

