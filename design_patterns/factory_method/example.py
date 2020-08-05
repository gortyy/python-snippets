from math import cos, sin


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def cartesian_point(cls, x: float, y: float):
        return cls(x, y)

    @classmethod
    def polar_point(cls, rho: float, theta: float):
        return cls(rho * cos(theta), rho * sin(theta))

    def __str__(self):
        return f"({self.x}, {self.y})"


if __name__ == "__main__":
    cartesian = Point.cartesian_point(2, 3)
    print(cartesian)

    polar = Point.polar_point(4, 45)
    print(polar)
