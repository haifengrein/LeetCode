#
# @lc app=leetcode.cn id=1343 lang=python3
#
# [1343] 大小为 K 且平均值大于等于阈值的子数组数目
#

# @lc code=start
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr_sum = sum(arr[:k])
        count = 0
        if curr_sum / k >= threshold:
            count += 1
        for right in range(k,len(arr)):
            curr_sum = curr_sum + arr[right] - arr[right - k]
            if curr_sum / k >= threshold:
                count +=1
        return count
        
        
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        curr_sum = sum(arr[:k])
        count = 0
        if curr_sum  >= threshold:
            count += 1
        for right in range(k,len(arr)):
            curr_sum = curr_sum + arr[right] - arr[right - k]
            if curr_sum >= threshold:
                count +=1
        return count

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = count = curr_sum = 0

        for right in range(len(arr)):
            curr_sum += arr[right]
            if right - left + 1 == k:
                if curr_sum / k >= threshold:
                    count += 1
                curr_sum -= arr[left]
                left +=1
        return count
        
        
# @lc code=end

