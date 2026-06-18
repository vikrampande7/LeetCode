class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        angle_minutes = 6 * minutes
        angle_hours = 30 * hour + 0.5 * minutes
        first_angle = abs(angle_hours - angle_minutes)
        second_angle = abs(360 - first_angle)
        print(first_angle, second_angle)
        return min(first_angle, second_angle)