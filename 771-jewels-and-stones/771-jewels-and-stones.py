class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        i = 0
        count = 0
        x = 0
        while i < len(jewels):
            if jewels[i] in stones:
                x += stones.count(jewels[i])
            i = i + 1
        return x