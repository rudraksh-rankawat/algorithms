class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        currentSum = 0
        left = 0
        right = 0
        shortest = float('inf')

        while right < len(nums):
            currentSum += nums[right]
            
            if currentSum >= target:
                
                while currentSum >= target:
                    currentSum -= nums[left]
                    left += 1
                shortest = min(shortest, right - left + 2)

            right += 1

        if shortest == float('inf'):
            return 0
        return shortest
