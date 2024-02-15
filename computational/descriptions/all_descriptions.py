from computational.descriptions.circle_three_points_description import CircleThreePointsDescription
from computational.descriptions.line_two_points_description import LineTwoPointsDescription
from computational.descriptions.point_free_description import PointFreeDescription


class AllDescriptions:
    lst = [PointFreeDescription, LineTwoPointsDescription, CircleThreePointsDescription]

    @staticmethod
    def get_all_descriptions():
        return AllDescriptions.lst