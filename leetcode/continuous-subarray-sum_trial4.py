class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        num_sum = 0
        rem_dict = {0:-1}

        for i in range(len(nums)):
            num_sum += nums[i]
            rem = num_sum % k

            if(rem in rem_dict):
                if i - rem_dict[rem] > 1:
                    return True
            else:
                rem_dict[rem] = i
        
        return False
