class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ans = steps = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                steps += 1
            ans += steps

        return ans