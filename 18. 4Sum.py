class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
            
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                a, b = j+1, len(nums)-1
                while a < b:
                    sum = nums[i] + nums[j] + nums[a] + nums[b]
                    if sum > target:
                        b -= 1
                    elif sum < target:
                        a += 1
                    else:
                        result.append([nums[i], nums[j], nums[a], nums[b]])
                        a += 1
                        while nums[a] == nums[a - 1] and a < b:
                            a += 1
        return result

                
        