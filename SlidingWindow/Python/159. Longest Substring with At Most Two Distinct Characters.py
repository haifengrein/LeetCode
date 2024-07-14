#
# @lc app=leetcode.cn id=159 lang=python3
# @lcpr version=30204
#
# [159] 至多包含两个不同字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (56.40%)
# Likes:    231
# Dislikes: 0
# Total Accepted:    38.6K
# Total Submissions: 68.4K
# Testcase Example:  '"eceba"'
#
# 给你一个字符串 s ，请你找出 至多 包含 两个不同字符 的最长子串，并返回该子串的长度。
# 
# 
# 示例 1：
# 
# 输入：s = "eceba"
# 输出：3
# 解释：满足题目要求的子串是 "ece" ，长度为 3 。
# 
# 
# 示例 2：
# 
# 输入：s = "ccaabbb"
# 输出：5
# 解释：满足题目要求的子串是 "aabbb" ，长度为 5 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 由英文字母组成
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = {}
        left,ans = 0,0
        for right, char in enumerate(s):
            window[char] = window.get(char,0) +1
            if len(window) <= 2:
                ans = max(ans,right - left +1)
            while len(window) > 2:
                window[s[left]] -=1
                if window[s[left]] == 0:
                    del window[s[left]]
                left+=1
        return ans
            
            
        
# @lc code=end



#
# @lcpr case=start
# "eceba"\n
# @lcpr case=end

# @lcpr case=start
# "ccaabbb"\n
# @lcpr case=end

#

