class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        ans = []

        for i in range(len(arr)):
            if arr[i] != 0:
                ans.append(arr[i])
            else:
                ans.append(0)
                ans.append(0)

        for i in range(len(arr)):
            arr[i] = ans[i]