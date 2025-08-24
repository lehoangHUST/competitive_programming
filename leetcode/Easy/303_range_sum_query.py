class NumArray:

    def __init__(self, nums: List[int]):
        self.pool = [0]
        for num in nums:
            self.pool.append(self.pool[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.pool[right + 1] - self.pool[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)