class Solution(object):
    def twoEditWords(self, queries, dictionary):
        """
        :type queries: List[str]
        :type dictionary: List[str]
        :rtype: List[str]
        """
        ans = []
        for q in queries:
            for d in dictionary:
                dist = 0
                for i in range(len(q)):
                    if q[i] != d[i]:
                        dist += 1
                if dist <= 2:
                    ans.append(q)
                    break
        return ans