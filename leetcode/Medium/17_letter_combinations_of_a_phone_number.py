class Solution:
    def merge_list(self, list_letter_digit1, list_letter_digit2) -> List[str]:
        results = []
        for letter_digit1 in list_letter_digit1:
            for letter_digit2 in list_letter_digit2:
                results.append(letter_digit1 + letter_digit2)
        return results


    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping_digits = {
            '2': 'a,b,c',
            '3': 'd,e,f',
            '4': 'g,h,i',
            '5': 'j,k,l',
            '6': 'm,n,o',
            '7': 'p,q,r,s',
            '8': 't,u,v',
            '9': 'w,x,y,z'
        }

        if len(digits):
            if digits in mapping_digits.keys():
                return mapping_digits[digits].split(',')
            else:
                letters_digits = []
                for digit in digits:
                    letters_digits.append(mapping_digits[digit].split(','))
                
                # T? h?p letter c?a các t? vi?t t?t
                results = []
                current = []
                for index in range(len(letters_digits)):
                    if index == 0:
                        results = letters_digits[index]
                    else:
                        results = self.merge_list(results, letters_digits[index])
                return results
        else:
            return []