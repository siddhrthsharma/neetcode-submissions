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
            i = 0
            while i < median:
                i+=1
            return self.arr[i]
        else:
            i = 0
            while i < median:
                i+=1
            return (self.arr[i-1] + self.arr[i]) / 2
        