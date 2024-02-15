from computational.descriptions.point_description import PointDescription


# example: let a = point_from_segment_ratio(b, c, 2, 3)
# point a is on segment bc and length(ab) / length(ac) = 2 / 3
class PointFromSegmentRatioDescription(PointDescription):
    code_line_template = "let {} = point_from_segment_ratio({}, {}, {}, {})"

    def __init__(self, name: object, dependencies):
        if len(dependencies) != 4:
            raise Exception("Incorrect number of dependencies for point")
        point1, point2, ratio1, ratio2 = dependencies
        if not point1.is_point() or not point2.is_point():
            raise Exception("Point from ratio first two arguments must be points")
        if not isinstance(ratio1, int) or not isinstance(ratio2, int) or ratio1 <= 0 or ratio2 <= 0:
            raise Exception("Both ratios must be positive integers")
        code_line = PointFromSegmentRatioDescription.code_line_template.format(name, point1.name, point2.name, ratio1, ratio2)
        super().__init__(name, code_line, dependencies)
