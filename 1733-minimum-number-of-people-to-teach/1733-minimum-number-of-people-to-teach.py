class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        teach = set()
        for f1, f2 in friendships:
            f1 -= 1
            f2 -= 1
            understand = False
            for l in languages[f1]:
                if l in languages[f2]:
                    understand = True
                    break
            if not understand:
                teach.add(f1)
                teach.add(f2)
        min_users = 1+len(languages)
        for l in range(1, n+1):
            count = 0
            for user in teach:
                if l not in languages[user]:
                    count += 1
            min_users = min(min_users, count)
        return min_users
