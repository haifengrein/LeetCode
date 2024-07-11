#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = Counter(p)
        k = len(p)
        s_len = len(s)
        s_count = Counter(s[:k])
        ans = []
        start = 0
        if s_count == p_count:
            ans.append(start)
        
        for right in range(k, s_len):
            s_count[s[right - k]] -= 1
            s_count[s[right]] += 1
            if s_count == p_count:
                ans.append(right -k +1)
        return ans
            

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def char_to_index(char):
            return ord(char) - 97

        p_count = [0] * 26
        s_count = [0] * 26
        k = len(p)
        s_len = len(s)
        ans = []

        if k > s_len:
            return ans

        # 初始化 p_count
        for char in p:
            p_count[char_to_index(char)] += 1

        # 初始化前 k 个字符的 s_count
        for i in range(k):
            s_count[char_to_index(s[i])] += 1

        if p_count == s_count:
            ans.append(0)

        for right in range(k, s_len):
            # 移除窗口左侧的字符
            s_count[char_to_index(s[right - k])] -= 1
            # 添加新的字符到窗口
            s_count[char_to_index(s[right])] += 1

            if p_count == s_count:
                ans.append(right - k + 1)

        return ans
# @lc code=end

