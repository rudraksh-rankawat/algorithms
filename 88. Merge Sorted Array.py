#best solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        fill = len(nums1) - 1
        a = m - 1
        b = n - 1

        while fill >= 0:

            if a == -1 or b == -1:
                break

            if nums1[a] > nums2[b]:
                nums1[fill] = nums1[a]
                a -= 1
            else:
                nums1[fill] = nums2[b]
                b -= 1
            fill -= 1

        if a == -1:
            while fill >= 0:
                nums1[fill] = nums2[b]
                fill -= 1
                b -= 1



        