class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, int(math.isqrt(c))

        while l <= r:
            s = l*l + r*r

            if s == c:
                return True
            elif s > c:
                r -= 1
            else:
                l += 1

        return False