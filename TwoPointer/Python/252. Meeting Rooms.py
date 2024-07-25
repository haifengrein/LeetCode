#
# @lc app=leetcode.cn id=252 lang=python3
# @lcpr version=30204
#
# [252] 会议室
#
# https://leetcode.cn/problems/meeting-rooms/description/
#
# algorithms
# Easy (58.57%)
# Likes:    162
# Dislikes: 0
# Total Accepted:    28.6K
# Total Submissions: 48.8K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给定一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi]
# ，请你判断一个人是否能够参加这里面的全部会议。
# 
# 
# 
# 示例 1：
# 
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：false
# 
# 
# 示例 2：
# 
# 输入：intervals = [[7,10],[2,4]]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
   def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
       intervals.sort()
       for i in range(len(intervals) - 1):
           if intervals[i][1] > intervals[i + 1][0]:
               return False
       return True
# @lc code=end



#
# @lcpr case=start
# [[0,30],[5,10],[15,20]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,10],[2,4]]\n
# @lcpr case=end

#

