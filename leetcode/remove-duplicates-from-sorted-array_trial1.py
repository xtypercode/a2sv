class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = 0
        while j < len(nums):
            if nums[j] != nums[i]:
                nums[i + 1] = nums[j]
                i += 1
            j += 1

        return i + 1 