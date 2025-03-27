# Go with the intuition look for logic
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = -1
        l, r = 0, len(height) - 1
        while l < r:
            minH = min(height[l], height[r])
            area = max(area, (r-l) * minH)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return area
        