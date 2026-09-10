class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        
    def findMedian(self) -> float:
        length = len(self.arr)
        median = length // 2
        if length % 2 != 0:
            return self.arr[median]
        else:
            return (self.arr[median-1] + self.arr[median]) / 2
        