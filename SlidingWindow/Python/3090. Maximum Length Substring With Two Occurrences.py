#
# @lc app=leetcode.cn id=3090 lang=python3
#
# [3090] 每个字符最多出现两次的最长子字符串
#

# @lc code=start
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = left = 0
        dic = {}
        for right in range(len(s)):
            if s[right] not in dic:
                dic[s[right]] = 1
            else:
                dic[s[right]] += 1
            while dic[s[right]] > 2:
                dic[s[left]] -= 1
                left += 1
            ans = max(ans,right-left+1)
        return ans
# @lc code=end

