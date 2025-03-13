class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ans = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1
        psum = 0
        for num in nums:
            psum = psum + num
            ans += hashmap.get(psum - k, 0)
            hashmap[psum] += 1

        return ans