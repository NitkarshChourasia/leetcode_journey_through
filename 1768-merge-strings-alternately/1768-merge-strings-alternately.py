class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        outputLst1 = []
        loopCountLst1 = [len(word1), len(word2)]
        #while (i < (len(word1) + len(word2))):
        while (i < max(loopCountLst1)):
            if i < len(word1):
                outputLst1.append(word1[i])
            if i < len(word2):    
                outputLst1.append(word2[i])
            i = i + 1
        outputAns = "".join(outputLst1)
        return outputAns


