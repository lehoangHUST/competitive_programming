

class Solution:
    def groupAnagrams(self, strs):

        strs_sort = [''.join(sorted(string)) for string in strs]
        set_strs = set(strs_sort)
        dict_anagrams = {}
        for set_str in set_strs:
            dict_anagrams[set_str] = [index for index, string in enumerate(strs_sort) if string == set_str]
        results = []

        for key, values in dict_anagrams.items():
            temp = []
            for value in values:
                temp.append(strs[value])
            results.append(temp)
        return results