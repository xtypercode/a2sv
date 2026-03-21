class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        ans = 0

        for i in range(len(word)):
            curr = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break

                curr.add(word[j])
                if len(curr) == 5:
                    ans += 1

        return ans