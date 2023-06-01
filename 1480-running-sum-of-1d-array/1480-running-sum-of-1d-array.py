class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 1
        outputAns = []
        while i <= len(nums):
            outputAns.append(sum(nums[:i]))
            i += 1
        return outputAns