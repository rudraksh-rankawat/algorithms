#took 12 mins


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        last = 0
        for i in range(len(nums)):
            if nums[last] == nums[i]:
                continue
            last += 1
            nums[last] = nums[i]

        
        return last + 1 #as last is 0 based index
