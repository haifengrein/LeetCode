#
# @lc app=leetcode.cn id=2958 lang=python3
# @lcpr version=30204
#
# [2958] 最多 K 个重复元素的最长子数组
#
# https://leetcode.cn/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
#
# algorithms
# Medium (54.00%)
# Likes:    14
# Dislikes: 0
# Total Accepted:    6.7K
# Total Submissions: 12.3K
# Testcase Example:  '[1,2,3,1,2,3,1,2]\n2'
#
# 给你一个整数数组 nums 和一个整数 k 。
# 
# 一个元素 x 在数组中的 频率 指的是它在数组中的出现次数。
# 
# 如果一个数组中所有元素的频率都 小于等于 k ，那么我们称这个数组是 好 数组。
# 
# 请你返回 nums 中 最长好 子数组的长度。
# 
# 子数组 指的是一个数组中一段连续非空的元素序列。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3,1,2,3,1,2], k = 2
# 输出：6
# 解释：最长好子数组是 [1,2,3,1,2,3] ，值 1 ，2 和 3 在子数组中的频率都没有超过 k = 2 。[2,3,1,2,3,1] 和
# [3,1,2,3,1,2] 也是好子数组。
# 最长好子数组的长度为 6 。
# 
# 
# 示例 2：
# 
# 输入：nums = [1,2,1,2,1,2,1,2], k = 1
# 输出：2
# 解释：最长好子数组是 [1,2] ，值 1 和 2 在子数组中的频率都没有超过 k = 1 。[2,1] 也是好子数组。
# 最长好子数组的长度为 2 。
# 
# 
# 示例 3：
# 
# 输入：nums = [5,5,5,5,5,5,5], k = 4
# 输出：4
# 解释：最长好子数组是 [5,5,5,5] ，值 5 在子数组中的频率没有超过 k = 4 。
# 最长好子数组的长度为 4 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 1 <= k <= nums.length
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        window = {}
        left, ans = 0, 0
        
        for right, num in enumerate(nums):
            window[num] = window.get(num,0) + 1
            while window[num] > k:
                window[nums[left]] -= 1
                left +=1
            ans = max(ans,right - left +1)
        return ans
                 
# @lc code=end
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        window = {}
        ans = 0
        invalid_count = 0  
        left = 0
        for right in range(len(nums)):

            num = nums[right]
            window[num] = window.get(num, 0) + 1
            if window[num] == k + 1:
                invalid_count += 1

            if invalid_count == 0:
                ans = max(ans, right - left + 1)

            while invalid_count > 0:
                window[nums[left]] -= 1
                if window[nums[left]] == k:
                    invalid_count -= 1
                left += 1

        return ans


#
# @lcpr case=start
# [1,2,3,1,2,3,1,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,1,2,1,2,1,2]\n1\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5,5,5,5]\n4\n
# @lcpr case=end

#

