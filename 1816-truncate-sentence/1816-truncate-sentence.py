class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        list1 = s.split()
        i = 0
        outputAns = []
        while i < k:
            outputAns.append(list1[i])
            i += 1
        return " ".join(outputAns)
        