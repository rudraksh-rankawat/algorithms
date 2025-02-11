import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()

        def isAlphaNum(c):
            return ((ord('A') <= ord(c) <= ord('Z')) or
             (ord('0') <= ord(c) <= ord('9')) or
             (ord('a') <= ord(c) <= ord('z')))

        start, end = 0, len(s) - 1

        if len(s) == 0 or (start == end):
            return True

        while start <= end:
            if not isAlphaNum(s[start]):
                start += 1
                continue

            if not isAlphaNum(s[end]):
                end -= 1
                continue

            if s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1

        return True

sol = Solution()
s = "race a car"
print(sol.isPalindrome(s))
        
# Solution 2
# import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:

#         s = s.lower()
#         reverseStr = s[::-1]

#         pattern = re.compile(r'[^a-zA-Z0-9]')

#         s = re.sub(pattern, '', s)
#         reverseStr = re.sub(pattern, '', reverseStr)

#         if s == reverseStr:
#             return True
#         return False

        
        

        