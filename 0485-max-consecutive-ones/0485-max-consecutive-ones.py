class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        final_count = 0
        for num in nums:
            if num == 1:
                count += 1
                final_count = max(final_count, count)
            else:
                count = 0
        return final_count