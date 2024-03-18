"""
    The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

    countAndSay(1) = "1"
    countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
    To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

    For example, the saying and conversion for digit string "3322251" => "23321511"
"""

import collections

class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        else:
            say = "1"
            start = 2
            while start <= n:
                string = ""
                count = 0
                char = say[0]
                for i in range(len(say)):
                    if say[i] == char:
                        count += 1
                    else:
                        string += f'{count}{char}'
                        char = say[i]
                        count = 1
                # Add substring from sequence last
                string += f'{count}{char}'
                say = string
                start += 1
            return say