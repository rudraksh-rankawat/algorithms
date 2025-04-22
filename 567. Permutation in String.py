import copy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        map1, map2 = {}, {}
        for c in s1:
            map1[c] = 1 + map1.get(c, 0)
        
        size_of_s1 = len(s1)
        l = 0

        for r in range(len(s2)):
            windowSize = r - l + 1
            map2[s2[r]] = 1 + map2.get(s2[r], 0)

            if windowSize == size_of_s1:
                if map1 == map2:
                    return True
                map2[s2[l]] -= 1
                if map2[s2[l]] == 0:
                    del map2[s2[l]]
                l += 1

        return False    


        
