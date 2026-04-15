class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = dict()
        for idx in range(len(s)):
            if s[idx] not in map:
                map[s[idx]] = []
            map[s[idx]].append(idx)

        for val in map:
            if len(map[val]) == 1:
                return map[val][0]

        return -1