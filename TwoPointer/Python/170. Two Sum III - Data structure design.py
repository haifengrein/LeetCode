#
# @lc app=leetcode.cn id=170 lang=python3
# @lcpr version=30204
#
# [170] 两数之和 III - 数据结构设计
#
# https://leetcode.cn/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (42.63%)
# Likes:    98
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 42.7K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# 设计一个接收整数流的数据结构，该数据结构支持检查是否存在两数之和等于特定值。
# 
# 实现 TwoSum 类：
# 
# 
# TwoSum() 使用空数组初始化 TwoSum 对象
# void add(int number) 向数据结构添加一个数 number
# boolean find(int value) 寻找数据结构中是否存在一对整数，使得两数之和与给定的值相等。如果存在，返回 true ；否则，返回
# false 。
# 
# 
# 
# 
# 示例：
# 
# 输入：
# ["TwoSum", "add", "add", "add", "find", "find"]
# [[], [1], [3], [5], [4], [7]]
# 输出：
# [null, null, null, null, true, false]
# 
# 解释：
# TwoSum twoSum = new TwoSum();
# twoSum.add(1);   // [] --> [1]
# twoSum.add(3);   // [1] --> [1,3]
# twoSum.add(5);   // [1,3] --> [1,3,5]
# twoSum.find(4);  // 1 + 3 = 4，返回 true
# twoSum.find(7);  // 没有两个整数加起来等于 7 ，返回 false
# 
# 
# 
# 提示：
# 
# 
# -10^5 <= number <= 10^5
# -2^31 <= value <= 2^31 - 1
# 最多调用 10^4 次 add 和 find
# 
# 
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class TwoSum:
    def __init__(self):
        self.hash_map = {}

    def add(self, number: int) -> None:
        self.hash_map[number] = self.hash_map.get(number, 0) + 1

    def find(self, value: int) -> bool:
        if len(self.hash_map) == 0:
            return False
        for key in self.hash_map.keys():
            diff = value - key
            if diff != key and diff in self.hash_map:
                return True
            if diff == key and self.hash_map[key] > 1:
                return True
        return False
            



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end
class TwoSum:
    def __init__(self):
        self.nums = set()
        self.sums = set()

    def add(self, number: int) -> None:
        for n in self.nums:
            self.sums.add(number + n)
        self.nums.add(number)

    def find(self, value: int) -> bool:
        return value in self.sums



#
# @lcpr case=start
# ["TwoSum", "add", "add", "add", "find", "find"][[], [1], [3], [5], [4], [7]]\n
# @lcpr case=end

#

