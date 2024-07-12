#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

# @lc code=start
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0: return []
        deque = collections.deque()
        
        # 处理初始窗口（前k个元素）
        for i in range(k):
            # 维护单调递减队列：移除所有小于当前元素的值
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        
        # 初始窗口的最大值（队首元素）
        res = [deque[0]]
        
        # 处理剩余元素，滑动窗口向右移动
        for i in range(k, len(nums)):
            # 如果窗口最左边的元素（将要移出窗口的元素）是当前最大值，将其从队列中移除
            if deque[0] == nums[i - k]:
                deque.popleft()
            
            # 继续维护单调递减队列
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            
            # 当前窗口的最大值（队首元素）加入结果列表
            res.append(deque[0])
        
        return res

# @lc code=end

