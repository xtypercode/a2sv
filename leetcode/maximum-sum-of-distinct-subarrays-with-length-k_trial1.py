class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = curr_sum = 0
        count = Counter()

        for i in range(len(nums)):
            curr_sum += nums[i]
            count[nums[i]] += 1

            if i >= k:
                left = nums[i - k]
                curr_sum -= left
                count[left] -= 1
                if count[left] == 0:
                    del count[left]

            if i >= k - 1:
                if len(count) == k:
                    ans = max(ans, curr_sum)
                    
        return ans