#
# @lc app=leetcode.cn id=3 lang=python3
# @lcpr version=30204
#
# [3] 无重复字符的最长子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, window = 0, {}
        left = 0
        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1

            # 核心逻辑：检查当前窗口是否全是不重复字符
            # 如果是，更新最大长度
            if len(window) == right - left + 1:
                max_len = max(max_len, right - left + 1)

            # 处理窗口中的重复字符
            # 移动左指针，直到删除重复字符，使窗口再次合法
            while right - left + 1 > len(window):
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
        return max_len

            
# @lc code=end
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = left = 0
        window = set()  # 维护当前窗口中的字符
        for right, c in enumerate(s):
            # 核心逻辑：移动左指针，直到窗口起始位置位于当前字符c的下一个位置
            # 这个过程会删除left到当前窗口实际起始位置之间的所有字符
            while c in window:
                window.remove(s[left])
                left += 1
            window.add(c)
            ans = max(ans, right - left + 1)
        return ans

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, hashmap = 0, {}
        start = 0
        for end in range(len(s)):
            # 更新字符最后出现的位置
            if s[end] in hashmap:
                # 更新start，确保start总是在最近的重复字符之后
                start = max(start, hashmap[s[end]] + 1)
            # 无论如何都要更新字符的位置
            hashmap[s[end]] = end
            # 更新最大长度
            max_len = max(max_len, end - start + 1)
        return max_len

#
# @lcpr case=start
# "abcabcbb"\n
# @lcpr case=end

# @lcpr case=start
# "bbbbb"\n
# @lcpr case=end

# @lcpr case=start
# "pwwkew"\n
# @lcpr case=end

#

