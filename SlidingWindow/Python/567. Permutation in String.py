#
# @lc app=leetcode.cn id=567 lang=python3
#
# [567] 字符串的排列
#

# @lc code=start
from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        k = len(s1)
        window_count = Counter(s2[:k])
        if window_count == s1_count:
            return True
        for right in range(k,len(s2)):
            window_count[s2[right - k]] -= 1
            window_count[s2[right]] +=1

            if window_count == s1_count:
                return True

        return False
    
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        # 填充 s1_count
        for char in s1:
            s1_count[ord(char) - ord('a')] += 1

        # 初始化窗口
        k = len(s1)
        for char in s2[:k]:
            window_count[ord(char) - ord('a')] += 1

        if s1_count == window_count:
            return True

        # 滑动窗口
        for right in range(k, len(s2)):
            # 移除窗口左侧的字符
            window_count[ord(s2[right - k]) - ord('a')] -= 1
            # 添加新的字符到窗口
            window_count[ord(s2[right]) - ord('a')] += 1

            if s1_count == window_count:
                return True

        return False

        
# @lc code=end

