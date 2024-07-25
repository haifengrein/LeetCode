#
# @lc app=leetcode.cn id=680 lang=python3
# @lcpr version=30204
#
# [680] 验证回文串 II
#
# https://leetcode.cn/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (40.27%)
# Likes:    645
# Dislikes: 0
# Total Accepted:    151.8K
# Total Submissions: 376.8K
# Testcase Example:  '"aba"'
#
# 给你一个字符串 s，最多 可以从中删除一个字符。
# 
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aba"
# 输出：true
# 
# 
# 示例 2：
# 
# 输入：s = "abca"
# 输出：true
# 解释：你可以删除字符 'c' 。
# 
# 
# 示例 3：
# 
# 输入：s = "abc"
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 由小写英文字母组成
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        def is_palin(s,i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        left, right = 0, len(s) -1
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        if left >= right:
            return True
        return is_palin(s,left + 1,right) or is_palin(s,left,right - 1)
        
# @lc code=end



#
# @lcpr case=start
# "aba"\n
# @lcpr case=end

# @lcpr case=start
# "abca"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n
# @lcpr case=end

#

