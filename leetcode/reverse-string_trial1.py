class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s)-1)

    def helper(self, s: List[str], l: int, r: int) -> None:
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        return self.helper(s, l + 1, r - 1)
        