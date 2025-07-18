class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 3
        heap = nums[2 * n:]
        curr = sum(heap)
        post = [curr]
        heapify(heap)
        for x in nums[2 * n - 1:n - 1:-1]:
            curr += x
            curr -= heappushpop(heap, x)
            post.append(curr)
        post.pop()

        heap = [-x for x in nums[:n]]
        heapify(heap)
        first = sum(heap)
        ans = -first - curr
        for x, second in zip(nums[n:2 * n], reversed(post)):
            first -= x
            first -= heappushpop(heap, -x)
            if (new := -first - second) < ans:
                ans = new
        return ans
        