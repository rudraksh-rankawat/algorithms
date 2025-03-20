class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue

            a, b = i+1, len(nums) - 1
            while a < b:
                

                sum = nums[a] + nums[b] + nums[i]
                if sum < 0:
                    a += 1
                elif sum > 0:
                    b -= 1
                else:
                    result.append([nums[i], nums[a], nums[b]])
                    a += 1
                    b -= 1
                    while a < b and nums[a] == nums[a - 1]:
                        a += 1
                    while a < b and nums[b] == nums[b + 1]:
                        b -= 1
                

        return result

