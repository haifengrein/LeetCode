#
# @lc app=leetcode.cn id=1876 lang=python3
#
# [1876] 长度为三且各字符不同的子字符串
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            temp_str = s[i:i+3]
            if len(set(temp_str)) == 3:
                count +=1
        return count
# @lc code=end

