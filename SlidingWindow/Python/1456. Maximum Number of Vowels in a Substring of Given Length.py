#
# @lc app=leetcode.cn id=1456 lang=python3
#
# [1456] 定长子串中元音的最大数目
#

# @lc code=start
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')
        count = sum(1 for char in s[:k] if char in vowel)
        max_count = count

        for right in range(k,len(s)):
            if s[right - k] in vowel:
                count -= 1
            if s[right] in vowel:
                count += 1
            if max_count < count:
                max_count = count
        return max_count
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set('aeiou')
        left = count = 0
        max_count = count

        for right in range(len(s)):
            if s[right] in vowel:
                count += 1
            
            if right - left + 1 == k:
                if max_count < count:
                    max_count = count
                
                if s[left] in vowel:
                    count -= 1
                left += 1
        return max_count

            

# @lc code=end

