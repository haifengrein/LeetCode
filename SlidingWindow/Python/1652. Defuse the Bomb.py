#
# @lc app=leetcode.cn id=1652 lang=python3
#
# [1652] 拆炸弹
#

# @lc code=start
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        res = [0] * n
        code *= 2

        if k > 0:
            left, right = 1, k + 1
        elif k < 0:
            left, right = n + k, n

        window_sum = sum(code[left:right])

        for i in range(n):
            res[i] = window_sum
            window_sum = window_sum + code[right] - code[left]
            left += 1
            right += 1
        return res

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        res = [0] * n
        code *= 2

        window_sum = sum(code[1:k+1] if k > 0 else code[n+k:n])
        
        for i in range(n):
            res[i] = window_sum
            window_sum -= code[i + 1 if k> 0 else n+k+i]
            window_sum += code[k + i + 1 if k>0 else n + i ]
        return res


# @lc code=end

