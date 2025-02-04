# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low, high = 1, n
        bad_version = -1
        while low <= high:
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                bad_version = mid
                high = mid - 1
            else:
                low = mid + 1
        return bad_version