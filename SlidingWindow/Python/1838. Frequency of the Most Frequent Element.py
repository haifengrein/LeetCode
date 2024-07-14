#
# @lc app=leetcode.cn id=1838 lang=python3
# @lcpr version=30204
#
# [1838] 最高频元素的频数
#
# https://leetcode.cn/problems/frequency-of-the-most-frequent-element/description/
#
# algorithms
# Medium (43.01%)
# Likes:    302
# Dislikes: 0
# Total Accepted:    39.4K
# Total Submissions: 91.6K
# Testcase Example:  '[1,2,4]\n5'
#
# 元素的 频数 是该元素在一个数组中出现的次数。
# 
# 给你一个整数数组 nums 和一个整数 k 。在一步操作中，你可以选择 nums 的一个下标，并将该下标对应元素的值增加 1 。
# 
# 执行最多 k 次操作后，返回数组中最高频元素的 最大可能频数 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,4], k = 5
# 输出：3
# 解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
# 4 是数组中最高频元素，频数是 3 。
# 
# 示例 2：
# 
# 输入：nums = [1,4,8,13], k = 5
# 输出：2
# 解释：存在多种最优解决方案：
# - 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
# - 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
# - 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。
# 
# 
# 示例 3：
# 
# 输入：nums = [3,9,6], k = 2
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^5
# 1 <= k <= 10^5
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()  # 对数组进行排序
        left = 0
        window_sum = 0
        max_freq = 0
        
        for right in range(len(nums)):
            window_sum += nums[right]
            
            # 计算将窗口内所有元素变成右边界元素所需的操作次数
            while (right - left + 1) * nums[right] - window_sum > k:
                window_sum -= nums[left]
                left += 1
            
            # 更新最大频率
            max_freq = max(max_freq, right - left + 1)
        
        return max_freq
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n5\n
# @lcpr case=end

# @lcpr case=start
# [1,4,8,13]\n5\n
# @lcpr case=end

# @lcpr case=start
# [3,9,6]\n2\n
# @lcpr case=end

#

