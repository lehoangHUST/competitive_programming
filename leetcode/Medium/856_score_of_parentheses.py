class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        score = 0
        # s consists of only '(' and ')' 
        for char in s:
            if char == '(':
                stack.append(score)
                score = 0
            else:
                if score:
                    score = 2 * score
                else:
                    score = 1
                
                score += stack.pop()
        
        return score