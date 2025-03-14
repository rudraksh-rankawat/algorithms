class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if not -1 < index < len(nums):
                continue

            if nums[index] == 0:
                nums[index] = (len(nums) + 1) * -1
            else:
                if nums[index] < 0:
                    continue
                nums[index] = nums[index] * -1

            
        for i in range(1, len(nums) + 1, 1):
            if not nums[i-1] < 0:
                return i

        return len(nums) + 1