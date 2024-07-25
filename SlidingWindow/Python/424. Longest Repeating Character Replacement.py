#
# @lc app=leetcode.cn id=424 lang=python3
# @lcpr version=30204
#
# [424] 替换后的最长重复字符
#
# https://leetcode.cn/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (55.07%)
# Likes:    865
# Dislikes: 0
# Total Accepted:    99.9K
# Total Submissions: 181.4K
# Testcase Example:  '"ABAB"\n2'
#
# 给你一个字符串 s 和一个整数 k 。你可以选择字符串中的任一字符，并将其更改为任何其他大写英文字符。该操作最多可执行 k 次。
# 
# 在执行上述操作后，返回 包含相同字母的最长子字符串的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
# 
# 
# 示例 2：
# 
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
# 可能存在其他的方法来得到同样的结果。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 仅由大写英文字母组成
# 0 <= k <= s.length
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,ans = 0, 0
        cnt = {}
        max_count = 0
        for right in range(len(s)):
            cnt[s[right]] = cnt.get(s[right],0) +1

            if cnt[s[right]] > max_count:
                max_count = cnt[s[right]]

            if right - left + 1 - max_count > k:
                cnt[s[left]] -= 1
                left +=1
            ans = max(ans,right -left + 1)
        return ans

# @lc code=end



#
# @lcpr case=start
# "ABAB"\n2\n
# @lcpr case=end

# @lcpr case=start
# "AABABBA"\n1\n
# @lcpr case=end

#

