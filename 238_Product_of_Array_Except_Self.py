
# from typing import List


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         totalProd = 1
#         for n in nums:
#             totalProd *= n
#         print(totalProd)
#         result = []

#         for i, n in enumerate(nums):
#             if n != 0:
#                 result.append(int(totalProd / n))
#             else:
#                 tempProd = 1
#                 for y, num in enumerate(nums):
#                     if y == i:
#                         continue
#                     tempProd *= num
#                 result.append(totalProd)

#         return result
        
# sol = Solution()
# nums = [-1,1,0,-3,3]
# result = sol.productExceptSelf(nums)
# print(result)


#OG solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        fromFirst, fromLast = [1 for i in range(len(nums))], [1 for i in range(len(nums))]

        temp = 1
        for i in range(len(nums)):
            temp *= nums[i]
            fromFirst[i] = temp

        temp = 1
        for i in range(len(nums)-1, -1, -1):
            temp *= nums[i]
            fromLast[i] = temp

        result = []

        left, right = 1, 1
        for i, num in enumerate(nums):
            if i-1 > -1:
                left = fromFirst[i-1]
            else:
                left = 1

            if i+1 < len(nums):
                right = fromLast[i+1]
            else:
                right = 1

            result.append(left * right)

        return result
        