class Solution:
    def maxTurbulenceSize(self, arr: List[int]) ->  int:
        if len(arr) < 2:
            return len(arr)
        
        ans, l = 1, 0
        for r in range(1, len(arr)):
            if arr[r] == arr[r-1]:
                l = r
            elif r == 1:
                pass
            else:
                a, b, c = arr[r-2], arr[r-1], arr[r]

                if (a < b < c) or (a > b > c):
                    l = r-1

            ans = max(ans, r-l+1)

        return ans
