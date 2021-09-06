class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        i = 0
        j = 1
        intervals.sort()
        while j < len(intervals):
            # if the next intervals lower number is less than or equal to
            # the current highest, they overlap, and have to be merged
            lower = min(intervals[i][0], intervals[j][0])
            higher = max(intervals[i][1], intervals[j][1])
            if intervals[j][0] <= intervals[i][1]:
                intervals[i][0] = lower
                intervals[i][1] = higher
                intervals.pop(j)
            else:
                i += 1
                j += 1
        return intervals
