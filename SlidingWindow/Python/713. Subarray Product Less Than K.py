#
# @lc app=leetcode.cn id=713 lang=python3
# @lcpr version=30204
#
# [713] 乘积小于 K 的子数组
#
# https://leetcode.cn/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (50.94%)
# Likes:    787
# Dislikes: 0
# Total Accepted:    120.5K
# Total Submissions: 236.5K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
# 
# 
# 示例 1：
# 
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,2,3], k = 0
# 输出：0
# 
# 
# 
# 提示: 
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        count, left = 0, 0
        curr_product = 1
        
        for right, num in enumerate(nums):
            curr_product *= num
            while curr_product >= k:
                curr_product //= nums[left]
                left+=1
            count += right - left + 1
        return count 
# @lc code=end



#
# @lcpr case=start
# [10,5,2,6]\n100\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n0\n
# @lcpr case=end

#

