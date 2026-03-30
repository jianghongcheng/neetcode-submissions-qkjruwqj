class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sumset = set(nums)
        longest = 0
        for num in nums:
            if (num-1) not in sumset:
                length = 1
                while (num + length) in sumset:
                    length += 1
                longest = max(longest, length)
        return longest