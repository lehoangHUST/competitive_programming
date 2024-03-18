class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0]) # sort
        stack = []
        stack.append(intervals[0])

        for interval in intervals[1:]:
            if stack[-1][0] <= interval[0] <= stack[-1][-1]:
                stack[-1][-1] = max(interval[-1], stack[-1][-1])
            else:
                stack.append(interval)
        
        return stack