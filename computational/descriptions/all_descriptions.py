from computational.descriptions.circle_description import CircleDescription
from computational.descriptions.line_description import LineDescription
from computational.descriptions.point_description import PointDescription


class AllDescriptions:
    lst = [PointDescription, LineDescription, CircleDescription]

    @staticmethod
    def get_all_descriptions():
        return AllDescriptions.lst