#
# @lc app=leetcode.cn id=76 lang=python3
# @lcpr version=30204
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (45.94%)
# Likes:    2934
# Dislikes: 0
# Total Accepted:    597.1K
# Total Submissions: 1.3M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
# 
# 
# 
# 注意：
# 
# 
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
# 
# 
# 示例 2：
# 
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
# 
# 
# 示例 3:
# 
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
# 
# 
# 
# 提示：
# 
# 
# ^m == s.length
# ^n == t.length
# 1 <= m, n <= 10^5
# s 和 t 由英文字母组成
# 
# 
# 
# 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        cnt_t = Counter(t)
        window_count = defaultdict(int)

        required = len(cnt_t)
        formed = 0

        min_len = inf
        min_start = 0
        left = 0

        for right, char in enumerate(s):
            window_count[char] += 1

            if char in cnt_t and window_count[char] == cnt_t[char]:
                formed += 1
            
            while left <= right and formed == required:
                if right - left +1 < min_len:
                    min_len, min_start = right - left + 1, left
                
                window_count[s[left]] -= 1
                if s[left] in cnt_t and window_count[s[left]] < cnt_t[s[left]]:
                    formed -= 1
                left += 1
        return "" if min_len == inf else s[min_start:min_start+min_len]

# @lc code=end
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        cnt_s = Counter()
        cnt_t = Counter(t)

        min_lenght = inf
        min_start = 0
        left = 0

        for right, char in enumerate(s):
            cnt_s[char] += 1
            while cnt_s >= cnt_t:
                if right - left + 1 < min_lenght:
                    min_lenght = right - left + 1
                    min_start = left
                
                cnt_s[s[left]] -= 1
                left +=1
        return "" if min_lenght == inf else s[min_start:min_lenght+min_start]



        



#
# @lcpr case=start
# "ADOBECODEBANC"\n"ABC"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"a"\n
# @lcpr case=end

# @lcpr case=start
# "a"\n"aa"\n
# @lcpr case=end

#

