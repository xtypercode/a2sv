class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        freq = Counter()
        left = pairs = ans = 0
        
        for right in range(len(nums)):
            pairs += freq[nums[right]]
            freq[nums[right]] += 1
            
            while pairs >= k:
                ans += len(nums) - right
                
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]
                left += 1
        
        return ans