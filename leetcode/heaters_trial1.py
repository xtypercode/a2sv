class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        ans = i = 0
        
        for house in houses:
            while i + 1 < len(heaters) and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1
            ans = max(ans, abs(heaters[i] - house))
            
        return ans
