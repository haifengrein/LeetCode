#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()
        left = ans = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 1:
                left +=1
            if nums[right] - nums[left] == 1:
                ans = max(ans, right-left + 1)
        return ans
    
    
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        record = Counter(nums)
        max_len = 0
        for num in record:
            if num + 1 in record:
                curr_len = record[num] + record[num +1]
                max_len = max(max_len, curr_len)
        return max_len
    


# @lc code=end

