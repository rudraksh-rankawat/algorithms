class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        newStr = ''
        i = 0
        while i < len(word1):

            newStr += word1[i]
            if i < len(word2):
                newStr += word2[i]
            i += 1

        if i < len(word2):
            newStr += word2[i:]

        return newStr