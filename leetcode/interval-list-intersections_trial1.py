class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []

        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            a, b = firstList[i], secondList[j]
            if a[1] < b[0]:
                i += 1

            elif a[0] > b[1]:
                j += 1

            elif a[1] <= b[1]:
                ans.append([max(a[0], b[0]), min(a[1], b[1])]) 
                i += 1

            elif b[1] <= a[1]:
                ans.append([max(a[0], b[0]), min(a[1], b[1])]) 
                j += 1

            else:
                i, j = i + 1, j + 1

        return ans