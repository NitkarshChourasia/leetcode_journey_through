class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        keyNoCopy = ""
        for letter in key:
            if letter not in keyNoCopy:
                keyNoCopy += letter
                
        keyNoCopy1 = keyNoCopy.replace(" ", "")
        
        outputLst1 = [""] * len(message)
        
        asciiLetters = [chr(x) for x in range(97, 122+1)]
        
        for i, ele in enumerate(message):
            try:
                outputLst1[i] = asciiLetters[keyNoCopy1.index(ele)]
            except:
                outputLst1[i] = " "
        return "".join(outputLst1)
        
        # The error is spaces I want to catch that error and divert it.