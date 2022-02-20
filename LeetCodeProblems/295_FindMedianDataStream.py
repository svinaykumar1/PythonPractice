class meadian_finder(object):
    def __init__(self):
        self.a=[]
    def addNum(self,i):
        self.a.append(i)
        print(self.a)
        return self.a

    def FindMedian(self):
        if(len(self.a)%2==0):
            median=(self.a[len(self.a)//2-1]+self.a[len(self.a)//2])/2
        else:
            median=self.a[len(self.a)//2]
        print(median)
        return median



MedianFinder=meadian_finder()
MedianFinder.addNum(1)
MedianFinder.addNum(2)
MedianFinder.FindMedian()
MedianFinder.addNum(3)
MedianFinder.FindMedian()