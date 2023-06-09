class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        # To count.
        # [Typei, Colori, Namei]
        i = 0
        count = 0
        while i < len(items):
            if ruleKey == "type":
                if ruleValue == items[i][0]:
                    count += 1
            elif ruleKey == "color":
                if ruleValue == items[i][1]:
                    count += 1
            elif ruleKey == "name":
                if ruleValue == items[i][2]:
                    count += 1
            i += 1
        return count