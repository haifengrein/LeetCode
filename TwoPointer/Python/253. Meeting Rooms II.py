#
# @lc app=leetcode.cn id=253 lang=python3
# @lcpr version=30204
#
# [253] 会议室 II
#
# https://leetcode.cn/problems/meeting-rooms-ii/description/
#
# algorithms
# Medium (52.57%)
# Likes:    605
# Dislikes: 0
# Total Accepted:    73.3K
# Total Submissions: 139.5K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# 给你一个会议时间安排的数组 intervals ，每个会议时间都会包括开始和结束的时间 intervals[i] = [starti, endi] ，返回
# 所需会议室的最小数量 。
# 
# 
# 
# 示例 1：
# 
# 输入：intervals = [[0,30],[5,10],[15,20]]
# 输出：2
# 
# 
# 示例 2：
# 
# 输入：intervals = [[7,10],[2,4]]
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= intervals.length <= 10^4
# 0 <= starti < endi <= 10^6
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        room =  0
        end_ptr = 0

        for start in starts:
            room += 1
            if start >= ends[end_ptr]:
                room -= 1
                end_ptr +=1
        return room
# @lc code=end



#
# @lcpr case=start
# [[0,30],[5,10],[15,20]]\n
# @lcpr case=end

# @lcpr case=start
# [[7,10],[2,4]]\n
# @lcpr case=end

#

