#
# @lc app=leetcode.cn id=1984 lang=python3
#
# [1984] 学生分数的最小差值
#

# @lc code=start
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        min_diff = float('inf')
        for right in range(len(nums)):
            if right - left + 1 == k:
                curr_diff = nums[right] - nums[left]
                min_diff = min(min_diff,curr_diff)
                left+= 1
        return min_diff
    
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        
        min_diff = float('inf')
        for start in range(n-k+1):
            curr_diff = nums[start + k -1] - nums[start]
            min_diff = min(min_diff,curr_diff)
        return min_diff
# @lc code=end

