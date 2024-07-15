# LeetCode进度追踪器
[English](README.md) | [中文](README_chinese.md)

## 问题类别统计
- 滑动窗口: 33 题
- 数组: 6 题
- 哈希表: 3 题
- 双指针: 1 题

## 难度统计
- 简单: 12 题
- 中等: 17 题
- 困难: 4 题

本仓库追踪我的LeetCode解题进度,主要使用Python语言。

## 已完成的问题

### 滑动窗口

#### 固定大小滑动窗口
| 题号 | 题目名称 | 最优时间复杂度 | 一句话解决方案摘要 |
|------|----------|----------------|---------------------|
| 187 | [重复的DNA序列](./SlidingWindow/Python/187.%20Repeated%20DNA%20Sequences.py) | O(n) | 使用滑动窗口和哈希映射计数10字母序列,返回出现次数超过一次的序列 |
| 219 | [存在重复元素 II](./SlidingWindow/Python/219.contains-duplicate-ii.py) | O(n) | 维护一个大小为k的哈希集合,随窗口滑动更新并检查重复元素 |
| 239 | [滑动窗口最大值](./SlidingWindow/Python/239.%20Sliding%20Window%20Maximum.py) | O(n) | 使用双端队列维护单调递减队列,滑动窗口并更新最大值 |
| 346 | [数据流中的移动平均值](./SlidingWindow/Python/346.%20Moving%20Average%20from%20Data%20Stream.py) | O(1) | 使用循环缓冲区(双端队列)维护固定大小的窗口,更新总和和平均值 |
| 438 | [找到字符串中所有字母异位词](./SlidingWindow/Python/438.%20Find%20All%20Anagrams%20in%20a%20String.py) | O(n) | 使用固定大小的数组计数字符,滑动窗口并比较计数 |
| 567 | [字符串的排列](./SlidingWindow/Python/567.%20Permutation%20in%20String.py) | O(n) | 使用固定大小的数组进行字符计数,滑动窗口并比较计数 |
| 643 | [子数组最大平均数 I](./SlidingWindow/Python/643.%20Maximum%20Average%20Subarray%20I.py) | O(n) | 初始化为前k个元素的和,然后滑动并更新最大平均值 |
| 1052 | [爱生气的书店老板](./SlidingWindow/Python/1052.%20Grumpy%20Bookstore%20Owner.py) | O(n) | 滑动窗口找到最大额外满意客户数,加到基础满意数上 |
| 1176 | [健身计划评估](./SlidingWindow/Python/1176.%20Diet%20Plan%20Performance.py) | O(n) | 滑动k大小的窗口,比较总和与边界,相应更新得分 |
| 1343 | [大小为 K 且平均值大于等于阈值的子数组数目](./SlidingWindow/Python/1343.%20Number%20of%20Sub-arrays%20of%20Size%20K%20and%20Average%20Greater%20than%20or%20Equal%20to%20Threshold.py) | O(n) | 滑动k大小的窗口,计算平均值,计数满足条件的子数组 |
| 1456 | [定长子串中元音的最大数目](./SlidingWindow/Python/1456.%20Maximum%20Number%20of%20Vowels%20in%20a%20Substring%20of%20Given%20Length.py) | O(n) | 滑动k大小的窗口,计数元音,更新最大元音数 |
| 1652 | [拆炸弹](./SlidingWindow/Python/1652.%20Defuse%20the%20Bomb.py) | O(n) | 计算初始k和,然后滑动并使用循环属性更新 |
| 1876 | [长度为三且各字符不同的子字符串](./SlidingWindow/Python/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters.py) | O(n) | 滑动3字符窗口,使用集合检查唯一性,计数有效子串 |
| 1984 | [学生分数的最小差值](./SlidingWindow/Python/1984.%20Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores.py) | O(nlogn) | 排序,然后滑动k大小的窗口找到最大值和最小值之间的最小差值 |
| 2090 | [半径为 k 的子数组平均值](./SlidingWindow/Python/2090.%20K%20Radius%20Subarray%20Averages.py) | O(n) | 计算前缀和,然后使用滑动窗口计算平均值 |
| 2269 | [找到一个数字的 K 美丽值](./SlidingWindow/Python/2269.%20Find%20the%20K-Beauty%20of%20a%20Number.py) | O(n) | 滑动k大小的窗口,将子串转换为整数,检查可除性,计数美丽值 |
| 2379 | [得到 K 个黑块的最少涂色次数](./SlidingWindow/Python/2379.%20Minimum%20Recolors%20to%20Get%20K%20Consecutive%20Black%20Blocks.py) | O(n) | 计算k窗口中初始白块数,滑动并更新所需的最小重新着色次数 |

#### 可变大小滑动窗口
| 题号 | 题目名称 | 最优时间复杂度 | 一句话解决方案摘要 |
|------|----------|----------------|---------------------|
| 3 | [无重复字符的最长子串](./SlidingWindow/Python/3.Longest%20Substring%20Without%20Repeating%20Characters.py) | O(n) | 使用哈希映射跟踪字符位置,无重复时扩展窗口并更新最大长度 |
| 76 | [最小覆盖子串](./SlidingWindow/Python/76.%20Minimum%20Window%20Substring.py) | O(m+n) | 使用两个指针和哈希映射跟踪字符计数,扩展和收缩窗口以找到覆盖t中所有字符的最小子串 |
| 159 | [至多包含两个不同字符的最长子串](./SlidingWindow/Python/159.%20Longest%20Substring%20with%20At%20Most%20Two%20Distinct%20Characters.py) | O(n) | 使用哈希映射计数字符,扩展窗口直到不同字符<=2,更新最大长度 |
| 209 | [长度最小的子数组](./SlidingWindow/Python/209.%20Minimum%20Size%20Subarray%20Sum.py) | O(n) | 使用两个指针维护滑动窗口,扩展右侧和收缩左侧以找到和>=目标的最小长度子数组 |
| 340 | [至多包含 K 个不同字符的最长子串](./SlidingWindow/Python/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters.py) | O(n) | 使用哈希映射计数字符,扩展窗口直到不同字符<=k,更新最大长度 |
| 424 | [替换后的最长重复字符](./SlidingWindow/Python/424.%20Longest%20Repeating%20Character%20Replacement.py) | O(n) | 使用带字符计数映射的滑动窗口,跟踪最大字符计数,扩展窗口直到(窗口大小-最大计数)<=k |
| 594 | [最长和谐子序列](./SlidingWindow/Python/594.%20Longest%20Harmonious%20Subsequence.py) | O(nlogn) | 排序数组,使用两个指针维护窗口使最大值-最小值=1,更新最大长度 |
| 713 | [乘积小于 K 的子数组](./SlidingWindow/Python/713.%20Subarray%20Product%20Less%20Than%20K.py) | O(n) | 使用两个指针,维护窗口元素的乘积,扩展右侧和收缩左侧以计数乘积<k的子数组 |
| 904 | [水果成篮](./SlidingWindow/Python/904.%20Fruit%20Into%20Baskets.py) | O(n) | 使用哈希映射跟踪两种水果的最后位置,更新最大长度 |
| 992 | [K 个不同整数的子数组](./SlidingWindow/Python/992.%20Subarrays%20with%20K%20Different%20Integers.py) | O(n) | 运用滑动窗口和包含-排除原理,通过相减最多K个和最多K-1个不同整数的子数组数量来找到恰好K个不同整数的子数组 |
| 1004 | [最大连续1的个数 III](./SlidingWindow/Python/1004.%20Max%20Consecutive%20Ones%20III.py) | O(n) | 计数零,扩展窗口直到零的数量<=k,更新连续1的最大长度 |
| 1234 | [替换子串得到平衡字符串](./SlidingWindow/Python/1234.%20Replace%20the%20Substring%20for%20Balanced%20String.py) | O(n) | 计数字符,使用滑动窗口找到平衡所需替换的最小子串 |
| 1248 | [统计「优美子数组」](./SlidingWindow/Python/1248.%20Count%20Number%20of%20Nice%20Subarrays.py) | O(n) | 应用滑动窗口和包含-排除原理,通过相减最多K-1个和最多K个奇数的子数组数量来找到恰好含K个奇数的子数组 |
| 1438 | [绝对差不超过限制的最长连续子数组](./SlidingWindow/Python/1438.%20Longest%20Continuous%20Subarray%20With%20Absolute%20Diff%20Less%20Than%20or%20Equal%20to%20Limit.py) | O(n) | 使用两个双端队列跟踪最小值和最大值,扩展窗口直到最大值-最小值<=限制,更新最大长度 |
| 1838 | [最高频元素的频数](./SlidingWindow/Python/1838.%20Frequency%20of%20the%20Most%20Frequent%20Element.py) | O(nlogn) | 排序数组,使用滑动窗口找到增量和<=k时的最大频率 |
| 2760 | [最长奇偶子数组](./SlidingWindow/Python/2760.%20Longest%20Even%20Odd%20Subarray%20With%20Threshold.py) | O(n) | 双指针: 扩展窗口直到奇偶交替且<=阈值,更新最大长度 |
| 2958 | [最多 K 个重复元素的最长子数组](./SlidingWindow/Python/2958.%20Length%20of%20Longest%20Subarray%20With%20at%20Most%20K%20Frequency.py) | O(n) | 使用哈希映射计数频率,扩展窗口直到所有频率<=k,更新最大长度 |
| 3090 | [每个字符最多出现两次的最长子字符串](./SlidingWindow/Python/3090.%20Maximum%20Length%20Substring%20With%20Two%20Occurrences.py) | O(n) | 扩展右侧,当字符计数>2时收缩左侧,更新最大长度,使用哈希映射计数 |
