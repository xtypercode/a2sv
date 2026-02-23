class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        d_idx = [[-1, -1], [-1, 0], [-1, +1], [0, -1], [0, +1], [+1, -1], [+1, 0], [+1, +1]]
        ans = []

        for i in range(len(img)):
            row = []
            for j in range(len(img[0])):
                count = 1
                sum = img[i][j]
                for [x, y] in d_idx:
                    if(0 <= i + x < len(img) and 0 <= j + y < len(img[0])):
                        count += 1
                        sum += img[i+x][j+y]
                row.append(floor(sum/count))
            ans.append(row)

        return ans
