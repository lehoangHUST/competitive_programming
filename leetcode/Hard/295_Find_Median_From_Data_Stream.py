class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        length = len(self.data)
        self.data.sort()
        if length % 2 == 1:
            return float(self.data[length // 2])
        else:
            # length is even
            return float(self.data[length // 2] + self.data[length // 2 - 1]) / 2
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()