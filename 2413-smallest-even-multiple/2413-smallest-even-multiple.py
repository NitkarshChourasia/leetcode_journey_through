class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i = 1
        multiply = 0
        while True:
            multiply = n * i
            if multiply % 2 == 0 and multiply % n == 0:
                break
            i += 1
        return multiply
            