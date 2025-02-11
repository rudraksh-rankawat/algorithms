#neetcode solution with bucket sort, time: 0(1), space: 0(1)
#other solutions: 1. classic brute force by sorting 0(nlogn), 2. heap 0(klogn) (recommended)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}
        freq = []

        for i in range(len(nums) + 1):
            freq.append([])

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result


        