class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. Reading in and ignore any leading whitespace
        s = s.strip()
        
        # 2. Check sign in string number
        sign = False
        if len(s):
            if s[0] == '+':
                    s = s.replace('+', '', 1)
            elif s[0] == '-':
                s = s.replace('-', '', 1)
                sign = True
        else:
            return 0

        # 3. Convert string to number
        if len(s):
            if s[0] < '0' or s[0] > '9':
                return 0
            else:
                string_number = ""
                for char in s:
                    if '0' <= char <= '9':
                        string_number += char
                    else:
                        break

                if sign:
                    if -int(string_number) < -pow(2, 31):
                        return -pow(2, 31)
                    else:
                        return -int(string_number)
                else:
                    if int(string_number) > pow(2, 31) - 1:
                        return pow(2, 31) - 1
                    else:
                        return int(string_number)
        else:
            return 0