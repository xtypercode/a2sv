class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMost(k):
            window = Counter()
            left = ans = 0
            
            for right in range(len(nums)):
                window[nums[right]] = window.get(nums[right], 0) + 1
                
                while len(window) > k:
                    window[nums[left]] -= 1
                    if window[nums[left]] == 0:
                        del window[nums[left]]
                        
                    left += 1
                
                ans += (right - left + 1)
            
            return ans
        
        return atMost(k) - atMost(k - 1)