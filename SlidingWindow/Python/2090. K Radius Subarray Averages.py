#
# @lc app=leetcode.cn id=2090 lang=python3
#
# [2090] 半径为 k 的子数组平均值
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        window = 2 * k + 1
        
        if k == 0:
            return nums
        if window > n:
            return [-1] * n
        
        ans = [-1] * n
        curr_sum = sum(nums[:window])
        
        for i in range(k, n - k):
            ans[i] = curr_sum // window
            if i < n - k - 1:
                curr_sum = curr_sum - nums[i-k] + nums[i+k+1]
        
        return ans
# @lc code=end

