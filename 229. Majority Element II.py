#try constant hashmap appraoch as well

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        majorEle1 = majorEle2 = count1 = count2 = 0
        
        for num in nums:
            if num == majorEle1:
                count1 += 1
            elif num == majorEle2:
                count2 += 1
            elif count1 == 0:
                count1 += 1
                majorEle1 = num
            elif count2 == 0:
                count2 += 1
                majorEle2 = num
            else:
                count1 -= 1
                count2 -= 1

        count1 = count2 = 0

        for num in nums:
            if num == majorEle1:
                count1 += 1
            if num == majorEle2:
                count2 += 1
        
        res = []

        if count1 > len(nums) // 3:
            res.append(majorEle1)
        if count2 > len(nums) // 3 and majorEle1 != majorEle2:
            res.append(majorEle2) 

        return res

        