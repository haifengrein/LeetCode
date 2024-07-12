# LeetCode Progress Tracker
[English](README.md) | [中文](README_chinese.md)

## Problem Category Statistics
- Sliding Window: 20 problems
- Array: 6 problems
- Hash Table: 3 problems
- Two Pointers: 1 problem

## Difficulty Statistics
- Easy: 12 problems
- Medium: 7 problems
- Hard: 1 problem

This repository tracks my LeetCode problem-solving progress, primarily using Python.

## Completed Problems

### Sliding Window

#### Fixed-size Sliding Window
| Problem No. | Problem Name | Optimal Time Complexity | One-line Solution |
|-------------|--------------|-------------------------|---------------------------|
| 187 | [Repeated DNA Sequences](./SlidingWindow/Python/187.%20Repeated%20DNA%20Sequences.py) | O(n) | Use sliding window with hash map to count 10-letter sequences, return those occurring more than once |
| 219 | [Contains Duplicate II](./SlidingWindow/Python/219.contains-duplicate-ii.py) | O(n) | Maintain a hash set of size k, update and check for duplicates as window slides |
| 239 | [Sliding Window Maximum](./SlidingWindow/Python/239.%20Sliding%20Window%20Maximum.py) | O(n) | Use deque to maintain monotonic decreasing queue, slide window and update max values |
| 346 | [Moving Average from Data Stream](./SlidingWindow/Python/346.%20Moving%20Average%20from%20Data%20Stream.py) | O(1) | Use a circular buffer (deque) to maintain a fixed-size window, update sum and average |
| 438 | [Find All Anagrams in a String](./SlidingWindow/Python/438.%20Find%20All%20Anagrams%20in%20a%20String.py) | O(n) | Use fixed-size array to count chars, slide window and compare counts |
| 567 | [Permutation in String](./SlidingWindow/Python/567.%20Permutation%20in%20String.py) | O(n) | Use fixed-size arrays for char counts, slide window and compare counts |
| 643 | [Maximum Average Subarray I](./SlidingWindow/Python/643.%20Maximum%20Average%20Subarray%20I.py) | O(n) | Initialize with first k elements' sum, then slide and update max average |
| 1052 | [Grumpy Bookstore Owner](./SlidingWindow/Python/1052.%20Grumpy%20Bookstore%20Owner.py) | O(n) | Slide window to find max additional satisfied customers, add to base satisfied count |
| 1176 | [Diet Plan Performance](./SlidingWindow/Python/1176.%20Diet%20Plan%20Performance.py) | O(n) | Slide k-size window, compare sum with bounds, update score accordingly |
| 1343 | [Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](./SlidingWindow/Python/1343.%20Number%20of%20Sub-arrays%20of%20Size%20K%20and%20Average%20Greater%20than%20or%20Equal%20to%20Threshold.py) | O(n) | Slide k-size window, calculate average, count subarrays meeting condition |
| 1456 | [Maximum Number of Vowels in a Substring of Given Length](./SlidingWindow/Python/1456.%20Maximum%20Number%20of%20Vowels%20in%20a%20Substring%20of%20Given%20Length.py) | O(n) | Slide k-size window, count vowels, update max vowel count |
| 1652 | [Defuse the Bomb](./SlidingWindow/Python/1652.%20Defuse%20the%20Bomb.py) | O(n) | Calculate initial k-sum, then slide and update using circular property |
| 1876 | [Substrings of Size Three with Distinct Characters](./SlidingWindow/Python/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters.py) | O(n) | Slide 3-char window, use set to check uniqueness, count valid substrings |
| 1984 | [Minimum Difference Between Highest and Lowest of K Scores](./SlidingWindow/Python/1984.%20Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores.py) | O(nlogn) | Sort, then slide k-size window to find minimum difference between max and min |
| 2090 | [K Radius Subarray Averages](./SlidingWindow/Python/2090.%20K%20Radius%20Subarray%20Averages.py) | O(n) | Calculate prefix sum, then use sliding window to compute averages |
| 2269 | [Find the K-Beauty of a Number](./SlidingWindow/Python/2269.%20Find%20the%20K-Beauty%20of%20a%20Number.py) | O(n) | Slide k-size window, convert substring to int, check divisibility, count beauties |
| 2379 | [Minimum Recolors to Get K Consecutive Black Blocks](./SlidingWindow/Python/2379.%20Minimum%20Recolors%20to%20Get%20K%20Consecutive%20Black%20Blocks.py) | O(n) | Count initial white blocks in k-window, slide and update min recolors needed |

#### Variable-size Sliding Window
| Problem No. | Problem Name | Optimal Time Complexity | One-line Solution Summary |
|-------------|--------------|-------------------------|---------------------------|
| 594 | [Longest Harmonious Subsequence](./SlidingWindow/Python/594.%20Longest%20Harmonious%20Subsequence.py) | O(nlogn) | Sort array, use two pointers to maintain window where max-min=1, update max length |
| 2760 | [Longest Even Odd Subarray With Threshold](./SlidingWindow/Python/2760.%20Longest%20Even%20Odd%20Subarray%20With%20Threshold.py) | O(n) | Two pointers: expand while alternating even-odd and <= threshold, update max length |  
| 3090 | [Maximum Length Substring With Two Occurrences](./SlidingWindow/Python/3090.%20Maximum%20Length%20Substring%20With%20Two%20Occurrences.py) | O(n) | Expand right, contract left when char count > 2, update max length, use hash map to count |