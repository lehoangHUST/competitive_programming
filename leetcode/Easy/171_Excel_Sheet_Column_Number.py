class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        """
            A -> 1
            AA -> 27
            AB -> 28
            ZY -> 701
        """
        column = 0
        len_string = len(columnTitle)
        for idx, char in enumerate(columnTitle):
            column += 26 ** (len_string - idx - 1) * (ord(char) - ord('A') + 1)
        return column