#
# @lc app=leetcode.cn id=1248 lang=python3
# @lcpr version=30204
#
# [1248] 统计「优美子数组」
#
# https://leetcode.cn/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (58.84%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    57.7K
# Total Submissions: 98.1K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# 给你一个整数数组 nums 和一个整数 k。如果某个连续子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。
# 
# 请返回这个数组中 「优美子数组」 的数目。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,2,1,1], k = 3
# 输出：2
# 解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
# 
# 
# 示例 2：
# 
# 输入：nums = [2,4,6], k = 1
# 输出：0
# 解释：数列中不包含任何奇数，所以不存在优美子数组。
# 
# 
# 示例 3：
# 
# 输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# 输出：16
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most(k):
            left, res = 0, 0
            for right, num in enumerate(nums):
                k -= num % 2
                while k < 0:
                    k += nums[left] % 2
                    left +=1
                res += right - left + 1
            return res
        return at_most(k) - at_most(k-1)
# @lc code=end



#
# @lcpr case=start
# [1,1,2,1,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,4,6]\n1\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2,1,2,2,1,2,2,2]\n2\n
# @lcpr case=end

#

