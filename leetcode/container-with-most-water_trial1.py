class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, ans, right = 0, 0, len(height)-1
        
        while left < right:
            w = right - left
            h = min(height[right], height[left])
            area = w * h
            ans = max(ans, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1 

        return ans