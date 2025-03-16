#gotta do again in place

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        arr1 = []
        for i in range(m):
            arr1.append(nums1[i])

        a = b = x = 0
        while a < len(arr1) and b < len(nums2):
            if arr1[a] < nums2[b]:
                nums1[x] = arr1[a]
                a += 1
            else: 
                nums1[x] = nums2[b]
                b += 1
            x += 1

        if a >= len(arr1):
            for i in range(b, len(nums2), 1):
                nums1[x] = nums2[i]
                x += 1

        if b >= len(nums2):
            for i in range(a, len(arr1), 1):
                nums1[x] = arr1[i]
                x += 1

        return nums1
            




        