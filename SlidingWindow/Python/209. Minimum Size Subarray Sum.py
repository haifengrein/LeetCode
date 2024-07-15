#
# @lc app=leetcode.cn id=209 lang=python3
# @lcpr version=30204
#
# [209] 长度最小的子数组
#
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (46.50%)
# Likes:    2169
# Dislikes: 0
# Total Accepted:    804.3K
# Total Submissions: 1.7M
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# 给定一个含有 n 个正整数的数组和一个正整数 target 。
# 
# 找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [numsl, numsl+1, ..., numsr-1, numsr]
# ，并返回其长度。如果不存在符合条件的子数组，返回 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：target = 7, nums = [2,3,1,2,4,3]
# 输出：2
# 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
# 
# 
# 示例 2：
# 
# 输入：target = 4, nums = [1,4,4]
# 输出：1
# 
# 
# 示例 3：
# 
# 输入：target = 11, nums = [1,1,1,1,1,1,1,1]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= target <= 10^9
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 
# 
# 
# 
# 进阶：
# 
# 
# 如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = inf
        left = 0
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_length = min(min_length, right - left +1)
                curr_sum -= nums[left]
                left += 1

        return min_length if min_length != inf else 0
        
# @lc code=end



#
# @lcpr case=start
# 7\n[2,3,1,2,4,3]\n
# @lcpr case=end

# @lcpr case=start
# 4\n[1,4,4]\n
# @lcpr case=end

# @lcpr case=start
# 11\n[1,1,1,1,1,1,1,1]\n
# @lcpr case=end

#

