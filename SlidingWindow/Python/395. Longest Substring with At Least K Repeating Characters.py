#
# @lc app=leetcode.cn id=395 lang=python3
# @lcpr version=30204
#
# [395] 至少有 K 个重复字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (52.59%)
# Likes:    905
# Dislikes: 0
# Total Accepted:    96.2K
# Total Submissions: 182.8K
# Testcase Example:  '"aaabb"\n3'
#
# 给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
# 
# 如果不存在这样的子字符串，则返回 0。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "aaabb", k = 3
# 输出：3
# 解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
# 
# 
# 示例 2：
# 
# 输入：s = "ababbc", k = 2
# 输出：5
# 解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^4
# s 仅由小写英文字母组成
# 1 <= k <= 10^5
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for unique in range(1, 27):  # 最多26个不同的字符
            char_count = {}
            left = 0
            valid_count = 0
            
            for right in range(len(s)):
                # 扩展窗口
                char = s[right]
                char_count[char] = char_count.get(char, 0) + 1
                if char_count[char] == k:
                    valid_count += 1
                
                # 收缩窗口
                while len(char_count) > unique:
                    left_char = s[left]
                    if char_count[left_char] == k:
                        valid_count -= 1
                    char_count[left_char] -= 1
                    if char_count[left_char] == 0:
                        del char_count[left_char]
                    left += 1
                
                # 更新结果
                if len(char_count) == unique == valid_count:
                    res = max(res, right - left + 1)
        
        return res
# @lc code=end



#
# @lcpr case=start
# "aaabb"\n3\n
# @lcpr case=end

# @lcpr case=start
# "ababbc"\n2\n
# @lcpr case=end

#

