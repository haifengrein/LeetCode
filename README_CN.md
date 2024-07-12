# LeetCode 进度追踪器
[English](README.md) | [中文](README_chinese.md)

## 问题类别统计
- 滑动窗口：20 题
- 数组：6 题
- 哈希表：3 题
- 双指针：1 题

## 难度统计
- 简单：12 题
- 中等：7 题
- 困难：1 题

本仓库跟踪我的 LeetCode 解题进度，主要使用 Python。

## 已完成的题目

### 滑动窗口

#### 固定大小滑动窗口
| 题号 | 题目名称 | 最优时间复杂度 | 一行解题摘要 |
|------|----------|----------------|--------------|
| 187 | [重复的DNA序列](./SlidingWindow/Python/187.%20Repeated%20DNA%20Sequences.py) | O(n) | 使用滑动窗口和哈希表计数10字母序列，返回出现多于一次的序列 |
| 219 | [存在重复元素 II](./SlidingWindow/Python/219.contains-duplicate-ii.py) | O(n) | 维护一个大小为k的哈希集合，滑动窗口更新并检查重复项 |
| 239 | [滑动窗口最大值](./SlidingWindow/Python/239.%20Sliding%20Window%20Maximum.py) | O(n) | 使用双端队列维护单调递减队列，滑动窗口并更新最大值 |
| 346 | [数据流中的移动平均值](./SlidingWindow/Python/346.%20Moving%20Average%20from%20Data%20Stream.py) | O(1) | 使用循环缓冲区（双端队列）维护固定大小的窗口，更新总和和平均值 |
| 438 | [找到字符串中所有字母异位词](./SlidingWindow/Python/438.%20Find%20All%20Anagrams%20in%20a%20String.py) | O(n) | 使用固定大小数组计数字符，滑动窗口并比较计数 |
| 567 | [字符串的排列](./SlidingWindow/Python/567.%20Permutation%20in%20String.py) | O(n) | 使用固定大小数组进行字符计数，滑动窗口并比较计数 |
| 643 | [子数组最大平均数 I](./SlidingWindow/Python/643.%20Maximum%20Average%20Subarray%20I.py) | O(n) | 初始化前k个元素的和，然后滑动并更新最大平均值 |
| 1052 | [爱生气的书店老板](./SlidingWindow/Python/1052.%20Grumpy%20Bookstore%20Owner.py) | O(n) | 滑动窗口找出最大额外满意顾客数，加到基础满意数上 |
| 1176 | [健身计划评估](./SlidingWindow/Python/1176.%20Diet%20Plan%20Performance.py) | O(n) | 滑动k大小的窗口，比较总和与边界，相应更新得分 |
| 1343 | [大小为 K 且平均值大于等于阈值的子数组数目](./SlidingWindow/Python/1343.%20Number%20of%20Sub-arrays%20of%20Size%20K%20and%20Average%20Greater%20than%20or%20Equal%20to%20Threshold.py) | O(n) | 滑动k大小的窗口，计算平均值，统计满足条件的子数组 |
| 1456 | [定长子串中元音的最大数目](./SlidingWindow/Python/1456.%20Maximum%20Number%20of%20Vowels%20in%20a%20Substring%20of%20Given%20Length.py) | O(n) | 滑动k大小的窗口，计数元音，更新最大元音数 |
| 1652 | [拆炸弹](./SlidingWindow/Python/1652.%20Defuse%20the%20Bomb.py) | O(n) | 计算初始k和，然后滑动并使用循环属性更新 |
| 1876 | [长度为三且各字符不同的子字符串](./SlidingWindow/Python/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters.py) | O(n) | 滑动3字符窗口，使用集合检查唯一性，计数有效子串 |
| 1984 | [学生分数的最小差值](./SlidingWindow/Python/1984.%20Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores.py) | O(nlogn) | 排序后，滑动k大小窗口找出最大值和最小值的最小差值 |
| 2090 | [半径为 k 的子数组平均值](./SlidingWindow/Python/2090.%20K%20Radius%20Subarray%20Averages.py) | O(n) | 计算前缀和，然后使用滑动窗口计算平均值 |
| 2269 | [找到一个数字的 K 美丽值](./SlidingWindow/Python/2269.%20Find%20the%20K-Beauty%20of%20a%20Number.py) | O(n) | 滑动k大小窗口，将子串转为整数，检查整除性，计数美丽值 |
| 2379 | [得到 K 个黑块的最少涂色次数](./SlidingWindow/Python/2379.%20Minimum%20Recolors%20to%20Get%20K%20Consecutive%20Black%20Blocks.py) | O(n) | 计数初始k窗口中的白块，滑动并更新最少重新着色次数 |

#### 可变大小滑动窗口
| 题号 | 题目名称 | 最优时间复杂度 | 一行解题摘要 |
|------|----------|----------------|--------------|
| 594 | [最长和谐子序列](./SlidingWindow/Python/594.%20Longest%20Harmonious%20Subsequence.py) | O(nlogn) | 排序数组，使用双指针维护最大值减最小值等于1的窗口，更新最大长度 |
| 2760 | [最长奇偶子数组](./SlidingWindow/Python/2760.%20Longest%20Even%20Odd%20Subarray%20With%20Threshold.py) | O(n) | 双指针：在奇偶交替且小于等于阈值的条件下扩展，更新最大长度 |  
| 3090 | [每个字符最多出现两次的最长子字符串](./SlidingWindow/Python/3090.%20Maximum%20Length%20Substring%20With%20Two%20Occurrences.py) | O(n) | 右指针扩展，当字符计数大于2时左指针收缩，更新最大长度，使用哈希表计数 |