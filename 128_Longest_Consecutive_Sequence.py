#love you

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        store = dict()
        ans = 0

        for num in nums:
            store[num] = store.get(num, 0)
        
        for key in store:
            if store[key] == 1:
                continue
            else:
                store[key]=1
                tempAns = 1
                ogKeyP1, ogKeyM1 = key+1, key-1
                while ogKeyP1 in store:
                    tempAns+=1
                    store[ogKeyP1]=1
                    ogKeyP1+=1
                while ogKeyM1 in store:
                    tempAns+=1
                    store[ogKeyM1]=1
                    ogKeyM1-=1

                if tempAns > ans:
                    ans = tempAns

        return ans

