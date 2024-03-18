class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Convert uppercase letters => lowercase letters 
        s = s.lower()

        # Step 2: Remove all character not in 'a' and 'z'
        s_char = ''
        for char in s:
            if 'a' <= char <= 'z' or '0' <= char <= '9' :
                s_char += char

        # Step 3: Check valid palindrome
        if len(s_char) == 0:
            return True
        else:
            half = len(s_char) // 2 if len(s_char) % 2 == 1 else len(s_char) // 2 - 1
            for i in range(half + 1):
                if s_char[i] != s_char[len(s_char) - i - 1]:
                    return False
            return True