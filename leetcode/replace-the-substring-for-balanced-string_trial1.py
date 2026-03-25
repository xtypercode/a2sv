class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        if all(count[c] == len(s)//4 for c in "QWER"):
            return 0

        left, ans = 0, len(s)
        for right in range(len(s)):
            count[s[right]] -= 1
            while left <= right and all(count[c] <= len(s)//4 for c in "QWER"): 
                ans = min(ans, right - left +1)
                count[s[left]] +=1
                left += 1
                
        return ans 