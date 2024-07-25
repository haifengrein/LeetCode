#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30204
#
# [26] 删除有序数组中的重复项
#
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (56.21%)
# Likes:    3571
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 3.3M
# Testcase Example:  '[1,1,2]'
#
# 给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持
# 一致 。然后返回 nums 中唯一元素的个数。
# 
# 考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：
# 
# 
# 更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums
# 的大小不重要。
# 返回 k 。
# 
# 
# 判题标准:
# 
# 系统会用下面的代码来测试你的题解:
# 
# int[] nums = [...]; // 输入数组
# int[] expectedNums = [...]; // 长度正确的期望答案
# 
# int k = removeDuplicates(nums); // 调用
# 
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
# ⁠   assert nums[i] == expectedNums[i];
# }
# 
# 如果所有断言都通过，那么您的题解将被 通过。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,1,2]
# 输出：2, nums = [1,2,_]
# 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
# 
# 
# 示例 2：
# 
# 输入：nums = [0,0,1,1,1,2,2,3,3,4]
# 输出：5, nums = [0,1,2,3,4]
# 解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4
# 。不需要考虑数组中超出新长度后面的元素。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -10^4 <= nums[i] <= 10^4
# nums 已按 非严格递增 排列
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i] 
                k += 1
        return k
# @lc code=end
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums)) 
        return len(nums)


#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

