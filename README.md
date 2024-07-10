# LeetCode Progress Tracker

[English](README.md) | [中文](README_chinese.md)

## Problem Category Statistics
- Sliding Window: 11 problems
- Array: 6 problems
- Hash Table: 3 problems
- Two Pointers: 1 problem

## Difficulty Statistics
- Easy: 11 problems
- Medium: 0 problems
- Hard: 0 problems

This repository tracks my LeetCode problem-solving progress, primarily using Python.

## Completed Problems

### Sliding Window

| Problem No. | Problem Name | Optimal Time Complexity | One-line Solution Summary |
|-------------|--------------|-------------------------|---------------------------|
| 219 | [Contains Duplicate II](./SlidingWindow/Python/219.contains-duplicate-ii.py) | O(n) | Use a hash table to maintain a sliding window of size k |
| 594 | [Longest Harmonious Subsequence](./SlidingWindow/Python/594.%20Longest%20Harmonious%20Subsequence.py) | O(n) | Use a hash table to count occurrences of each number, then iterate through the hash table |
| 643 | [Maximum Average Subarray I](./SlidingWindow/Python/643.%20Maximum%20Average%20Subarray%20I.py) | O(n) | Fixed-size sliding window of size k, maintaining the window sum |
| 1176 | [Diet Plan Performance](./SlidingWindow/Python/1176.%20Diet%20Plan%20Performance.py) | O(n) | Fixed-size sliding window of size k, calculate window sum and compare with upper and lower bounds |
| 1652 | [Defuse the Bomb](./SlidingWindow/Python/1652.%20Defuse%20the%20Bomb.py) | O(n) | Use prefix sum or sliding window to calculate the sum of k elements |
| 1876 | [Substrings of Size Three with Distinct Characters](./SlidingWindow/Python/1876.%20Substrings%20of%20Size%20Three%20with%20Distinct%20Characters.py) | O(n) | Fixed-size sliding window of size 3, check if characters in the window are unique |
| 1984 | [Minimum Difference Between Highest and Lowest of K Scores](./SlidingWindow/Python/1984.%20Minimum%20Difference%20Between%20Highest%20and%20Lowest%20of%20K%20Scores.py) | O(nlogn) | Sort, then use fixed-size sliding window of size k to find minimum difference |
| 2269 | [Find the K-Beauty of a Number](./SlidingWindow/Python/2269.%20Find%20the%20K-Beauty%20of%20a%20Number.py) | O(n) | Fixed-size sliding window of size k, convert substring to number and check divisibility |
| 2379 | [Minimum Recolors to Get K Consecutive Black Blocks](./SlidingWindow/Python/2379.%20Minimum%20Recolors%20to%20Get%20K%20Consecutive%20Black%20Blocks.py) | O(n) | Fixed-size sliding window of size k, count white blocks that need recoloring |
| 2760 | [Longest Even Odd Subarray With Threshold](./SlidingWindow/Python/2760.%20Longest%20Even%20Odd%20Subarray%20With%20Threshold.py) | O(n) | Two pointers to maintain the longest subarray satisfying the conditions |
| 3090 | [Maximum Length Substring With Two Occurrences](./SlidingWindow/Python/3090.%20Maximum%20Length%20Substring%20With%20Two%20Occurrences.py) | O(n) | Sliding window + hash table to count character occurrences, expand right pointer, contract left pointer |