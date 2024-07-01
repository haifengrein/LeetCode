#
# @lc app=leetcode.cn id=219 lang=python3
# @lcpr version=30204
#
# [219] 存在重复元素 II
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        window = set()
        left = 0
        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            
            window.add(nums[right])
        return False
    
class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dict = {}
        for index, num in enumerate(nums):
            if num in dict and index - dict[num] <=k :
                return True
            dict[num] = index
        return False
        
        
# @lc code=end



#
# @lcpr case=start
# [1,2,3,1]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,0,1,1]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1,2,3]\n2\n
# @lcpr case=end

#

