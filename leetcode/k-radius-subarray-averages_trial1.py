class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1] * len(nums)

        currWS = sum(nums[:2*k])
        for i in range(k, len(nums)-k):
            currWS += nums[i+k]
            ans[i] = currWS//(2*k+1)
            currWS -= nums[i-k]
            
        return ans