#
# @lc app=leetcode.cn id=2760 lang=python3
#
# [2760] 最长奇偶子数组
#

# @lc code=start
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n,ans,left = len(nums),0,0

        while left < n:
            if nums[left] % 2 != 0 or nums[left] > threshold:
                left+=1
                continue
            right, curr = left + 1, nums[left] % 2
            while right < n:
                if nums[right] > threshold or nums[right] % 2 == curr:break
                curr,right = nums[right] % 2, right + 1
            ans = max(ans, right - left)
            left = right

        return ans
# @lc code=end

