#
# @lc app=leetcode.cn id=1438 lang=python3
# @lcpr version=30204
#
# [1438] 绝对差不超过限制的最长连续子数组
#
# https://leetcode.cn/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/description/
#
# algorithms
# Medium (51.08%)
# Likes:    380
# Dislikes: 0
# Total Accepted:    53.7K
# Total Submissions: 105.2K
# Testcase Example:  '[8,2,4,7]\n4'
#
# 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于
# limit 。
# 
# 如果不存在满足条件的子数组，则返回 0 。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [8,2,4,7], limit = 4
# 输出：2 
# 解释：所有子数组如下：
# [8] 最大绝对差 |8-8| = 0 <= 4.
# [8,2] 最大绝对差 |8-2| = 6 > 4. 
# [8,2,4] 最大绝对差 |8-2| = 6 > 4.
# [8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
# [2] 最大绝对差 |2-2| = 0 <= 4.
# [2,4] 最大绝对差 |2-4| = 2 <= 4.
# [2,4,7] 最大绝对差 |2-7| = 5 > 4.
# [4] 最大绝对差 |4-4| = 0 <= 4.
# [4,7] 最大绝对差 |4-7| = 3 <= 4.
# [7] 最大绝对差 |7-7| = 0 <= 4. 
# 因此，满足题意的最长子数组的长度为 2 。
# 
# 
# 示例 2：
# 
# 输入：nums = [10,1,2,4,7,2], limit = 5
# 输出：4 
# 解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。
# 
# 
# 示例 3：
# 
# 输入：nums = [4,2,2,2,4,4,2,2], limit = 0
# 输出：3
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^9
# 0 <= limit <= 10^9
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()  # 存储窗口内的最大值
        min_deque = deque()  # 存储窗口内的最小值
        left = 0
        ans = 0

        for right in range(len(nums)):
            # 维护最大值队列
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)

            # 维护最小值队列
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)

            # 如果窗口内的最大值和最小值的差超过了limit，收缩窗口
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if left > max_deque[0]:
                    max_deque.popleft()
                if left > min_deque[0]:
                    min_deque.popleft()

            # 更新最长子数组长度
            ans = max(ans, right - left + 1)

        return ans
# @lc code=end



#
# @lcpr case=start
# [8,2,4,7]\n4\n
# @lcpr case=end

# @lcpr case=start
# [10,1,2,4,7,2]\n5\n
# @lcpr case=end

# @lcpr case=start
# [4,2,2,2,4,4,2,2]\n0\n
# @lcpr case=end

#

