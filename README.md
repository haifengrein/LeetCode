# LeetCode Progress Tracker
[English](README.md)

## Problem Category Statistics
- Sliding Window: 33 problems
- Array: 6 problems
- Hash Table: 3 problems
- Two Pointers: 13 problem

## Difficulty Statistics
- Easy: 18 problems
- Medium: 21 problems
- Hard: 4 problems

This repository tracks my LeetCode problem-solving progress, primarily using Python.

## Completed Problems

### Sliding Window

#### Fixed-size Sliding Window
| Problem No. | Problem Name | Optimal Time Complexity | One-line Solution Summary |
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
| 3 | [Longest Substring Without Repeating Characters](./SlidingWindow/Python/3.Longest%20Substring%20Without%20Repeating%20Characters.py) | O(n) | Use hash map to track char positions, expand window and update max length when no repeats |
| 76 | [Minimum Window Substring](./SlidingWindow/Python/76.%20Minimum%20Window%20Substring.py) | O(m+n) | Use two pointers and hash map to track character counts, expand and contract window to find minimum substring covering all characters in t |
| 159 | [Longest Substring with At Most Two Distinct Characters](./SlidingWindow/Python/159.%20Longest%20Substring%20with%20At%20Most%20Two%20Distinct%20Characters.py) | O(n) | Use hash map to count chars, expand window while distinct chars <= 2, update max length |
| 209 | [Minimum Size Subarray Sum](./SlidingWindow/Python/209.%20Minimum%20Size%20Subarray%20Sum.py) | O(n) | Use two pointers to maintain a sliding window, expand right and contract left to find minimum length subarray with sum >= target |
| 340 | [Longest Substring with At Most K Distinct Characters](./SlidingWindow/Python/340.%20Longest%20Substring%20with%20At%20Most%20K%20Distinct%20Characters.py) | O(n) | Use hash map to count chars, expand window while distinct chars <= k, update max length |
| 424 | [Longest Repeating Character Replacement](./SlidingWindow/Python/424.%20Longest%20Repeating%20Character%20Replacement.py) | O(n) | Use sliding window with character count map, track max character count, expand window while (window size - max count) <= k |
| 594 | [Longest Harmonious Subsequence](./SlidingWindow/Python/594.%20Longest%20Harmonious%20Subsequence.py) | O(nlogn) | Sort array, use two pointers to maintain window where max-min=1, update max length |
| 713 | [Subarray Product Less Than K](./SlidingWindow/Python/713.%20Subarray%20Product%20Less%20Than%20K.py) | O(n) | Use two pointers, maintain product of window elements, expand right and contract left to count subarrays with product < k |
| 904 | [Fruit Into Baskets](./SlidingWindow/Python/904.%20Fruit%20Into%20Baskets.py) | O(n) | Use hash map to track last positions of two types of fruits, update max length |
| 992 | [Subarrays with K Different Integers](./SlidingWindow/Python/992.%20Subarrays%20with%20K%20Different%20Integers.py) | O(n) | Employs sliding window and inclusion-exclusion, subtracting counts of at-most K-1 from K to find exactly K distinct integers |
| 1004 | [Max Consecutive Ones III](./SlidingWindow/Python/1004.%20Max%20Consecutive%20Ones%20III.py) | O(n) | Count zeros, expand window while zeros <= k, update max length of consecutive ones |
| 1234 | [Replace the Substring for Balanced String](./SlidingWindow/Python/1234.%20Replace%20the%20Substring%20for%20Balanced%20String.py) | O(n) | Count characters, use sliding window to find minimum substring to replace for balancing |
| 1248 | [Count Number of Nice Subarrays](./SlidingWindow/Python/1248.%20Count%20Number%20of%20Nice%20Subarrays.py) | O(n) | Applies sliding window and inclusion-exclusion, subtracting counts of at-most K-1 from K to find subarrays with exactly K odd numbers |
| 1438 | [Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit](./SlidingWindow/Python/1438.%20Longest%20Continuous%20Subarray%20With%20Absolute%20Diff%20Less%20Than%20or%20Equal%20to%20Limit.py) | O(n) | Use two deques to track min and max, expand window while max-min <= limit, update max length |
| 1838 | [Frequency of the Most Frequent Element](./SlidingWindow/Python/1838.%20Frequency%20of%20the%20Most%20Frequent%20Element.py) | O(nlogn) | Sort array, use sliding window to find max frequency while sum of increments <= k |
| 2760 | [Longest Even Odd Subarray With Threshold](./SlidingWindow/Python/2760.%20Longest%20Even%20Odd%20Subarray%20With%20Threshold.py) | O(n) | Two pointers: expand while alternating even-odd and <= threshold, update max length |
| 2958 | [Length of Longest Subarray With at Most K Frequency](./SlidingWindow/Python/2958.%20Length%20of%20Longest%20Subarray%20With%20at%20Most%20K%20Frequency.py) | O(n) | Use hash map to count frequencies, expand window while all frequencies <= k, update max length |
| 3090 | [Maximum Length Substring With Two Occurrences](./SlidingWindow/Python/3090.%20Maximum%20Length%20Substring%20With%20Two%20Occurrences.py) | O(n) | Expand right, contract left when char count > 2, update max length, use hash map to count |

### Two Pointers

| Problem No. | Problem Name | Optimal Time Complexity | One-line Solution Summary |
|-------------|--------------|-------------------------|---------------------------|
| 15 | [3Sum](./TwoPointer/Python/15.%203Sum.py) | O(n^2) | Sort array, fix one number and use two pointers to find the other two |
| 26 | [Remove Duplicates from Sorted Array](./TwoPointer/Python/26.%20Remove%20Duplicates%20from%20Sorted%20Array.py) | O(n) | Use two pointers, one to iterate through array, one to keep track of last unique element position |
| 27 | [Remove Element](./TwoPointer/Python/27.%20Remove%20Element.py) | O(n) | Use two pointers, one to iterate through array, one to keep track of elements not equal to val |
| 28 | [Find the Index of the First Occurrence in a String](./TwoPointer/Python/28.%20Find%20the%20Index%20of%20the%20First%20Occurrence%20in%20a%20String.py) | O((n-m+1)*m) | Traverse main string, compare substring, return index when match found |
| 88 | [Merge Sorted Array](./TwoPointer/Python/88.%20Merge%20Sorted%20Array.py) | O(m+n) | Compare elements from back to front, place larger one at the end of nums1 |
| 125 | [Valid Palindrome](./TwoPointer/Python/125.%20Valid%20Palindrome.py) | O(n) | Convert string to lowercase alphanumeric, then compare forward and backward |
| 167 | [Two Sum II - Input Array Is Sorted](./TwoPointer/Python/167.%20Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted.py) | O(n) | Use left and right pointers, move based on comparison with target sum |
| 170 | [Two Sum III - Data structure design](./TwoPointer/Python/170.%20Two%20Sum%20III%20-%20Data%20structure%20design.py) | O(n) add, O(n) find | Use hash table to store numbers and their counts, traverse hash table when finding |
| 252 | [Meeting Rooms](./TwoPointer/Python/252.%20Meeting%20Rooms.py) | O(nlogn) | Sort meeting times, check if adjacent meetings overlap |
| 253 | [Meeting Rooms II](./TwoPointer/Python/253.%20Meeting%20Rooms%20II.py) | O(nlogn) | Sort start and end times separately, use pointers to traverse and count concurrent meetings |
| 283 | [Move Zeroes](./TwoPointer/Python/283.%20Move%20Zeroes.py) | O(n) | Use two pointers, one traverses array, one records non-zero position, swap when non-zero found |
| 408 | [Valid Word Abbreviation](./TwoPointer/Python/408.%20Valid%20Word%20Abbreviation.py) | O(n) | Use two pointers to traverse word and abbr respectively, handle numeric abbreviations |
| 680 | [Valid Palindrome II](./TwoPointer/Python/680.%20Valid%20Palindrome%20II.py) | O(n) | Compare from both ends, when different chars found, try deleting left or right char and check palindrome |
