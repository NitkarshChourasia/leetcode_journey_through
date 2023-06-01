class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        i = 0
        total = []
        while i < len(accounts):
            total.append(sum(accounts[i]))
            i += 1
        return max(total)