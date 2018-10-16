"""
    Peter Casey
    Oct 15, 2018
    Simple Radix10 sort for numbers
"""

from queue2 import Queue

class Radix10_Sort():

    def max10(self, lst):
        """
           Find the longest number in the list
        :param lst:
        :return: the number of digits of the longest
        """
        largest = max(lst)
        return len(str(abs(largest)))


    def make_bins(self):
        """
            Create the 10 Queue bins for the sort
        :return: list of 10 bins
        """
        bins = []

        for i in range(10):
            bins.append(Queue())

        return bins

    def getDigit(self, x, p):
        """
            find the pth digit from the right in number x
            EX:  getDigit(1234, 2) ==> 3
        :param x:
        :param p:
        :return:
        """
        return x // 10**(p) % 10

    def sort(self, nums):
        bins = self.make_bins()

        # loop over the numbers the largest number of places
        for i in range(self.max10(nums)):
            # Grab the ith digit from each number put into ith bin
            for n in nums:
                bins[self.getDigit(n, i)].enqueue(n)

            # Clear the list of numbers
            #nums = []

            # Copy the numbers from the bins, in order, back into the cleared list
            # Clear each bin after it is emptied
            idx = 0
            for bin in bins:
                for i in range(bin.size()):
                    #nums.append(bin.dequeue())
                    nums[idx] = bin.dequeue()
                    idx += 1
                bin.clear()

        return nums



