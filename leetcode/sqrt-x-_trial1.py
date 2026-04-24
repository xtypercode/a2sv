class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        l, r = 2, x // 2
        while l <= r:
            m = l + (r - l) // 2
            num = m * m
            
            if num > x:
                r = m - 1
            elif num < x:
                l = m + 1
            else:
                return m
        
        return r
