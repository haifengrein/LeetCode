# LeetCode 进度跟踪器

[English](README.md) | [中文](README_chinese.md)

## 问题类别统计
- 滑动窗口: 11 题
- 数组: 6 题
- 哈希表: 3 题
- 双指针: 1 题

## 难度统计
- 简单: 11 题
- 中等: 0 题
- 困难: 0 题

此仓库跟踪我的 LeetCode 问题解决进度，主要使用 Python。

## 已完成的问题

### 滑动窗口

#### 定长滑动窗口

| 题号 | 题目名称 | 最优时间复杂度 | 一句话题解 |
|------|----------|----------------|------------|
| 219 | [存在重复元素 II](./SlidingWindow/Python/219.contains-duplicate-ii.py) | O(n) | 使用哈希表维护一个大小为k的滑动窗口 |
| 643 | [子数组最大平均数 I](./SlidingWindow/Python/643.%20Maximum%20Average%20Subarray%20I.py) | O(n) | 固定大小为k的滑动窗口，维护窗口和 |
| 1176 | [健身计划评估](./SlidingWindow/Python/1176.%20Diet%20Plan%20Performance.py) | O(n) | 固定大小为k的滑动窗口，计算窗口和并与上下限比较 |
| 1652 | [拆炸弹](./SlidingWindow/Python/1652.%20Defuse%20the%20Bomb.py) | O(n) | 使用前缀和或滑动窗口计算k个元素的和 |
| 1876 | [长度为三且各字符不同的子字符串](./SlidingWindow/Python/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters.py) | O(n) | 固定大小为3的滑动窗口，检查窗口内字符是否唯一 |
| 1984 | [学生分数的最小差值](./SlidingWindow/Python/1984.%20Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores.py) | O(nlogn) | 排序后使用固定大小为k的滑动窗口找最小差值 |
| 2269 | [找到一个数字的 K 美丽值](./SlidingWindow/Python/2269.%20Find%20the%20K-Beauty%20of%20a%20Number.py) | O(n) | 固定大小为k的滑动窗口，将子串转为数字并检查整除性 |
| 2379 | [得到 K 个黑块的最少涂色次数](./SlidingWindow/Python/2379.%20Minimum%20Recolors%20to%20Get%20K%20Consecutive%20Black%20Blocks.py) | O(n) | 固定大小为k的滑动窗口，统计需要涂色的白块数 |

#### 不定长滑动窗口

| 题号 | 题目名称 | 最优时间复杂度 | 一句话题解 |
|------|----------|----------------|------------|
| 594 | [最长和谐子序列](./SlidingWindow/Python/594.%20Longest%20Harmonious%20Subsequence.py) | O(n) | 使用哈希表统计每个数字出现次数，然后遍历哈希表 |
| 2760 | [最长奇偶子数组](./SlidingWindow/Python/2760.%20Longest%20Even%20Odd%20Subarray%20With%20Threshold.py) | O(n) | 双指针维护最长满足条件的子数组 |
| 3090 | [每个字符最多出现两次的最长子字符串](./SlidingWindow/Python/3090.%20Maximum%20Length%20Substring%20With%20Two%20Occurrences.py) | O(n) | 滑动窗口 + 哈希表统计字符出现次数，右指针扩展，左指针收缩 |