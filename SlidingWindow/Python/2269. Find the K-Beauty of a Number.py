#
# @lc app=leetcode.cn id=2269 lang=python3
#
# [2269] 找到一个数字的 K 美丽值
#

# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0
        left = 0
        for right in range(len(num_str)):
            if right - left + 1 == k:
                curr_int = int(num_str[left:right + 1])
                if curr_int  != 0 and num % int(curr_int ) == 0:
                    count += 1
                left += 1
        return count
    
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        count = 0
        n = len(num_str)

        for i in range(n-k+1):
            curr_int = int(num_str[i:i+k])
            if curr_int !=0 and num % curr_int == 0:
                count += 1
        return count

# @lc code=end

