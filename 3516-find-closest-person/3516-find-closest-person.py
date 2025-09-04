class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_steps = abs(z - x)
        y_steps = abs(z - y)

        if x_steps < y_steps:
            return 1
        if x_steps > y_steps:
            return 2
        else:
            return 0