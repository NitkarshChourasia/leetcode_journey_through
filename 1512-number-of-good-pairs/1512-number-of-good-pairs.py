class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i = 0
        j = 1
        count = 0
        while i < len(nums):
            while j < len(nums):
                if i < j:
                    if nums[i] == nums[j]:
                        count += 1
                j += 1
            j = 0
            i += 1
        return count
                    