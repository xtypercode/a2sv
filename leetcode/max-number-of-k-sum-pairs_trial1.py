class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)
        ans = 0

        for x in list(freq.keys()):
            y = k - x

            if x == y:
                ans += freq[x] // 2
            elif y in freq:
                pairs = min(freq[x], freq[y])
                ans += pairs
                freq[x] = 0
                freq[y] = 0

        return ans