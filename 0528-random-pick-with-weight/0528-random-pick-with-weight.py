class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum 
        

    def pickIndex(self):
        """
        :rtype: int
        """
        t = self.total_sum * random.random()
        for i, prefix_sum in enumerate(self.prefix_sums):
            if prefix_sum > t:
                return i

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()