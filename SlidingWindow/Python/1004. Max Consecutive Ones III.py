#
# @lc app=leetcode.cn id=1004 lang=python3
# @lcpr version=30204
#
# [1004] 最大连续1的个数 III
#
# https://leetcode.cn/problems/max-consecutive-ones-iii/description/
#
# algorithms
# Medium (59.47%)
# Likes:    711
# Dislikes: 0
# Total Accepted:    164.4K
# Total Submissions: 276.5K
# Testcase Example:  '[1,1,1,0,0,0,1,1,1,1,0]\n2'
#
# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
# 
# 示例 2：
# 
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# nums[i] 不是 0 就是 1
# 0 <= k <= nums.length
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        record = [0,0]
        left, ans = 0, 0
        for right ,num in enumerate (nums):
            record[num] += 1
            if record[0] <= k:
                ans = max(ans, right -left + 1)
            while record[0] > k:
                record[nums[left]] -=1
                left +=1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,1,1,0,0,0,1,1,1,1,0]\n2\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]\n3\n
# @lcpr case=end

#

