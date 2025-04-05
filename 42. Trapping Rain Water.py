#initial recusrsive thought and approach did not work becuase one direction approach
class Solution:
    def trap(self, height: List[int]) -> int:


        def recurse(last, area):
            cur = last + 1
            if cur >= len(height) - 1:
                return 0

            inLast = cur

            while height[cur] < height[last]:
                if cur >= len(height):
                    return 0
            
                if height[inLast] > height[cur]:
                    cur = recurse(inLast, area)
                inLast = cur
                cur += 1

            area += cur-last-1
            return cur

        
        curr = 0
        last = 0
        totalArea = 0

        while curr < len(height):
            if height[curr] >= height[last]:
                last = curr
                curr += 1
            else:
                area = 0
                curr = recurse(last, area)
                last = curr
                totalArea += area




        return totalArea
        
            
            
            
        