class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max_energy = float("-inf")
        for i in range(len(energy) - k, len(energy)):
            e = 0
            j = i
            while j >= 0:
                e += energy[j]
                j = j - k
                max_energy = max(e, max_energy)
        return max_energy