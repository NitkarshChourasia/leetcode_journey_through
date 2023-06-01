class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        i = 0
        x = 0
        while i < len(operations):
            if "-" in operations[i]:
                x -= 1
            elif "+" in operations[i]:
                x += 1
            i += 1
        return x
    
        