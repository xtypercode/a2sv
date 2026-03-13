class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_counter = [0]*26
        max_v = left = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord("A")
            s_counter[idx] += 1

            max_v = max(max_v, s_counter[idx])
            while (r - left + 1) - max_v > k:
                s_counter[ord(s[left]) - ord("A")] -= 1
                left += 1

        return r - left + 1

