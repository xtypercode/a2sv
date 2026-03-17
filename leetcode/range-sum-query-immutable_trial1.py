class NumArray:

    def __init__(self, nums: List[int]):
        self.ans = [nums[0]]

        for i in range(len(nums)):
            self.ans.append(self.ans[-1]+nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.ans[right+1] - self.ans[left]