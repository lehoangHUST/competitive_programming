class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for row in range(numRows):
            ans_row = []
            for i in range(row + 1):
                if i == 0 or i == row:
                    ans_row.append(1)
                else:
                    ans_row.append(ans[row - 1][i] + ans[row - 1][i - 1])
            ans.append(ans_row)
        return ans