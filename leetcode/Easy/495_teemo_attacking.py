class Solution:
    def merge_poison_duration(self, lists):
        stack = []
        stack.append(lists[0])

        for interval in lists[1:]:
            if stack[-1][0] <= interval[0] <= stack[-1][-1]:
                stack[-1][-1] = max(interval[-1], stack[-1][-1])
            else:
                stack.append(interval)
        return stack

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if duration == 0:
            return 0
        list_time_poison = []
        total_time_poison = 0
        for time in timeSeries:
            list_time_poison.append([time, time + duration - 1])
        list_merge_poison = self.merge_poison_duration(list_time_poison)
        for merge_poison in list_merge_poison:
            total_time_poison += merge_poison[1] - merge_poison[0] + 1
        return total_time_poison