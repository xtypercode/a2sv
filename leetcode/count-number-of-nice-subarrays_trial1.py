class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = left = odds = 0
        curr = 0
        
        for right in range(len(nums)):
            if nums[right] % 2 == 1:
                odds += 1
                curr = 0
                
            while odds == k:
                if nums[left] % 2 == 1:
                    odds -= 1
                curr += 1
                left += 1
                
            ans += curr
            
        return ans