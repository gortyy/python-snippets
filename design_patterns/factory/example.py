from math import cos, sin


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    class PointFactory:
        def cartesian_point(self, x: float, y: float):
            return Point(x, y)

        def polar_point(self, rho: float, theta: float):
            return Point(rho * cos(theta), rho * sin(theta))

    factory = PointFactory()


if __name__ == "__main__":
    cartesian = Point.factory.cartesian_point(2, 3)
    print(cartesian)

    polar = Point.factory.polar_point(4, 45)
    print(polar)
