class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:  
        if not nums:
            return 0
        longest = 1
        cur = 1
        nums = sorted(set(nums))
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                cur += 1
            else:
                longest = max(longest, cur)
                cur = 1

        return max(longest, cur)