class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        oneMistake = False
        hoGyaBhai = False
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if oneMistake:
                    hoGyaBhai = True
                    break
                oneMistake = True
                l += 1

        if hoGyaBhai:
            l, r = 0, len(s) - 1
            oneMistake = False
            while l < r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    if oneMistake:
                        return False
                    oneMistake = True
                    r -= 1


        return True

        