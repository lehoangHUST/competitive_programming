class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []
        for i_row in range(rowIndex + 1):
            ans_row = []
            for i in range(i_row + 1):
                if i == i_row or i == 0:
                    ans_row.append(1)
                else:
                    ans_row.append(ans[i_row - 1][i] + ans[i_row - 1][i - 1])
            ans.append(ans_row)
        print(ans)
        return ans[-1]