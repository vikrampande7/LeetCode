class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels_counter = {}
        cons_counter = {}

        for c in s:
            if c in "aeiou":
                vowels_counter[c] = 1 + vowels_counter.get(c, 0)
            else:
                cons_counter[c] = 1 + cons_counter.get(c, 0)

        v_heap = [(-v, k) for k, v in vowels_counter.items()]
        c_heap = [(-v, k) for k, v in cons_counter.items()]        

        heapq.heapify(v_heap)
        heapq.heapify(c_heap)
        print(v_heap)
        print(cons_counter)

        if not v_heap:
            return -(c_heap[0][0])
        elif not c_heap:
            return -(v_heap[0][0])
        else:
            return -(v_heap[0][0] + c_heap[0][0])