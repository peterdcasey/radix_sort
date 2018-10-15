from queue import Queue

def max10(lst):
    largest = max(lst)
    return len(str(abs(largest)))

def make_bins():
    bins = []

    for i in range(10):
        bins.append(Queue())

    return bins

def getDigit(x, p):
    return x // 10**(p) % 10

nums = [34, 5, 67, 82, 29, 401, 1, 14, 1000]
bins = make_bins()

for i in range(max10(nums)):
    for n in nums:
        bins[getDigit(n, i)].enqueue(n)
    nums = []

    for bin in bins:
        for i in range(bin.size()):
            nums.append(bin.dequeue())
        bin.clear()

print(nums)



