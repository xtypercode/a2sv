class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        ans, l, r = 0, 0, len(skill)-1
        signature = skill[l] + skill[r]

        while(l < r):
            if(skill[l] + skill[r] == signature):
                ans += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                ans = -1
                break

        return ans