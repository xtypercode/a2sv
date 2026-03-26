class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        ans, alphabet = [], "abcdefghijklmnopqrstuvwxyz"

        diff = [0] * (n+1)
        for start, end , direction in shifts:
            diff[start] += 1 if direction == 1 else -1
            diff[end+1] -= 1 if direction == 1 else -1

        for i in range(1,n+1):
            diff[i] += diff[i-1]

        for i in range(n):
            ans.append(alphabet[(ord(s[i])-ord('a') + diff[i]) % 26])

        return ''.join(ans)