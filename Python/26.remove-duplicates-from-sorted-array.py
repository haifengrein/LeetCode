#
# @lc app=leetcode.cn id=26 lang=python3
# @lcpr version=30203
#
# [26] 删除有序数组中的重复项
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1,len(nums)):
            if nums[left] == nums[right]:
                if nums[right + 1] != None:
                    nums[right] = nums[right +1]
                else:
                    nums[right] = None
            else:
                left = right
        return len(nums)
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,1,1,1,2,2,3,3,4]\n
# @lcpr case=end

#

