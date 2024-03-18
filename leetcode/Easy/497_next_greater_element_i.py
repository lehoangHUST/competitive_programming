class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # nums1 and nums2 are unique
        # Conditional : O(nums1.length + nums2.length)
        # O(nums2.length)
        dict_nums2 = {}
        results = []
        for i, num in enumerate(nums2):
            dict_nums2[num] = i

        key_nums2 = list(dict_nums2.keys())
        value_nums2 = list(dict_nums2.values())
        print(key_nums2)
        # O(nums1.length)
        for num in nums1:
            j = dict_nums2[num]
            if j == len(nums2) - 1:
                results.append(-1)
            else:
                m = max(key_nums2[j + 1:])
                if m > key_nums2[j]:
                    for v in key_nums2[j + 1:]:
                        if v > key_nums2[j]:
                            results.append(v)
                            break
                else:
                    results.append(-1)
        return results
