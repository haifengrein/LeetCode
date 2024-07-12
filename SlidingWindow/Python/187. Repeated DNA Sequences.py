#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
K = 10

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        cnt = defaultdict(int)
        for i in range(len(s) - K + 1):
            sub = s[i : i + K]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)
        return ans

# @lc code=end

