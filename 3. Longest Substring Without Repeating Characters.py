class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 1:
            return 1
        if not s:
            return 0

        maxSubstr = 0
        tempHash = set()
        currentSubstr = 0

        right = 0
        left = 0

        while right < len(s):
            if s[right] not in tempHash:
                tempHash.add(s[right])
                currentSubstr += 1
                right += 1
            else:
                tempHash.remove(s[left])
                currentSubstr -= 1
                left += 1

            maxSubstr = max(maxSubstr, currentSubstr)

        return maxSubstr

            
        