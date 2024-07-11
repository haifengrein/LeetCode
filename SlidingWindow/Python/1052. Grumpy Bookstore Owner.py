#
# @lc app=leetcode.cn id=1052 lang=python3
#
# [1052] 爱生气的书店老板
#

# @lc code=start
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = 0
        extra = 0
        
        for i in range(minutes):
            if grumpy[i]:
                extra += customers[i]
            else:
                satisfied += customers[i]
        
        max_extra = extra
        
        for i in range(minutes, len(customers)):
            if grumpy[i - minutes]:
                extra -= customers[i - minutes]
            if grumpy[i]:
                extra += customers[i]
                max_extra = max(max_extra, extra)
            else:
                satisfied += customers[i]
        
        return satisfied + max_extra
    
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        base_satisfied = 0
        window_sum = 0
        max_extra = 0

        for i in range(n):
            # 计算基础满意的顾客数
            if grumpy[i] == 0:
                base_satisfied += customers[i]
            
            # 计算当前窗口内额外满意的顾客数
            if i < minutes:
                window_sum += customers[i] * grumpy[i]
            else:
                # 滑动窗口
                window_sum += customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
            
            # 更新最大额外满意顾客数
            max_extra = max(max_extra, window_sum)

        return base_satisfied + max_extra
    
# @lc code=end

