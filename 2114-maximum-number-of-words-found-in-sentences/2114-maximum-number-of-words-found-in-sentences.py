class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        outputAns = []
        for i in sentences:
            outputAns.append(len(i.split(' ')))
        return max(outputAns)
            
            