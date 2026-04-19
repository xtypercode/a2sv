class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_val = deque() 
        max_val = deque()
        max_wind = left = 0
        
        for right in range(len(nums)):
            while max_val and nums[max_val[-1]] <= nums[right]:
                max_val.pop()

            max_val.append(right)
            while min_val and nums[min_val[-1]] >= nums[right]:
                min_val.pop()
            min_val.append(right)

            while nums[max_val[0]] - nums[min_val[0]] > limit:
                left += 1
                if max_val[0] < left:
                    max_val.popleft()
                if min_val[0] < left:
                    min_val.popleft()
            
            max_wind = max(max_wind, right - left + 1)
        
        return max_wind