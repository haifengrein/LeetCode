#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        min_count = blocks[:k].count('W')
        count = min_count
        for right in range(k,len(blocks)):
            if blocks[right] == 'W':
                count += 1
            if blocks[right - k] == 'W':
                count -= 1
            
            min_count = min(count,min_count)

        return min_count
    
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0
        left = 0
        min_count = float("inf")
        count = 0
        for right in range(len(blocks)):
            if blocks[right] == 'W':
                count += 1
            if right - left + 1 == k:
                min_count = min(count,min_count)
                if blocks[left] == 'W':
                    count -= 1
                left +=1
        return min_count

# @lc code=end

