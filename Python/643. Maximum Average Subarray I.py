#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) <= k:
            return sum(nums) / k
        curr_sum = max_sum = sum(nums[:k])
        for right in range(k,len(nums)):
            curr_sum = curr_sum + nums[right] - nums[right - k]
            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum / k
# @lc code=end

