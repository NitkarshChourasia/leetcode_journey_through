class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1 = max(candies)
        i = 0
        outputLst1 = []
        while i < len(candies):
            if candies[i] + extraCandies >= max1:
                outputLst1.append(True)
            elif candies[i] + extraCandies < max1:
                outputLst1.append(False)
            i = i + 1
        return outputLst1