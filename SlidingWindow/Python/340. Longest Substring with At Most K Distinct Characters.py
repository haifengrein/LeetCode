#
# @lc app=leetcode.cn id=340 lang=python3
# @lcpr version=30204
#
# [340] 至多包含 K 个不同字符的最长子串
#
# https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Medium (51.35%)
# Likes:    263
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 58.5K
# Testcase Example:  '"eceba"\n2'
#
# 给你一个字符串 s 和一个整数 k ，请你找出 至多 包含 k 个 不同 字符的最长子串，并返回该子串的长度。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "eceba", k = 2
# 输出：3
# 解释：满足题目要求的子串是 "ece" ，长度为 3 。
# 
# 示例 2：
# 
# 输入：s = "aa", k = 1
# 输出：2
# 解释：满足题目要求的子串是 "aa" ，长度为 2 。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = {}
        left, ans = 0, 0
        # 维护一个最多包含k个不同字符的滑动窗口，统计字符频次，超出k个字符时从左收缩窗口
        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0) + 1
            if len(window) <= k:
                ans = max(ans,right - left + 1)
            while len(window) > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left +=1
        return ans
# @lc code=end
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        window = {}
        left,ans = 0, 0
        # 用哈希表记录字符最新位置，超过k个字符时直接删除最早出现的字符并跳转左指针
        for right in range(len(s)):
            window[s[right]] = right
            if len(window) <= k:
                ans = max(ans,right- left + 1)
            if len(window) == k+1:
                min_val = min(window.values())
                del window[s[min_val]]
                left = min_val + 1
        return ans


#
# @lcpr case=start
# "eceba"\n2\n
# @lcpr case=end

# @lcpr case=start
# "aa"\n1\n
# @lcpr case=end

#

