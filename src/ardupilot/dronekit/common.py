import math

class Convert:
    @staticmethod
    def radian2degree(radian):
        """Convert radians to degrees."""
        if not isinstance(radian, (int, float)):
            raise ValueError("Input must be a number.")
        return float(radian * (180 / math.pi))

    @staticmethod
    def degree2radian(degree):
        """Convert degrees to radians."""
        if not isinstance(degree, (int, float)):
            raise ValueError("Input must be a number.")
        return float(degree * (math.pi / 180))
