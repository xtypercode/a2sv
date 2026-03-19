class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = defaultdict(int)
        ans = l = 0

        for r in range(len(fruits)):
            count[fruits[r]] += 1

            while len(count) > 2 and l < r:
                count[fruits[l]] -= 1
                if not count[fruits[l]]:
                    del count[fruits[l]]
                l += 1

            ans = max(ans, r - l + 1)
            r += 1
            
        return ans
