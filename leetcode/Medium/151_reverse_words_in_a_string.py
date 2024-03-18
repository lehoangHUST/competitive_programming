class Solution:
    def reverseWords(self, s: str) -> str:
        # Split word in string
        list_word = s.split()

        return ' '.join(list_word[::-1])