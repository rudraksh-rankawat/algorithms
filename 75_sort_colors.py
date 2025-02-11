# Solved 1st Time: 1.5 hour

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        s, e = 0, len(nums) - 1
        m = -1

        while s < e:

            if nums[s] > nums[e]:
                temp = nums[s]
                nums[s] = nums[e]
                nums[e] = temp
                print(nums)

            if m != -1: 
                if nums[e] > nums[m]:
                    temp = nums[e]
                    nums[e] = nums[m]
                    nums[m] = temp
                print(nums)


            
            #pointer replacements
            if nums[s] == 0:
                s += 1

            if nums[e] == 2:
                e -= 1

            if nums[s] == 1 and nums[e] == 1:
                if m == -1:
                    m = e
                e -= 1
                

            if nums[m] == 2:
                m -= 1

        print("ans: ", nums)



arr = [1,2,1]
# arr = [2,0,2,1,1,0]
sol = Solution()
sol.sortColors(arr)            









        