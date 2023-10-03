# https://www.codewars.com/kata/55dcdd2c5a73bdddcb000044/train/python

# Rectangles represented as [x0, y0, x1, y1]


class Rectangle:
    @staticmethod
    def get_area(rectangle_coords):
        width, height = abs(rectangle_coords[2] - rectangle_coords[0]), abs(rectangle_coords[3] - rectangle_coords[1])
        area = width * height
        return area


def calculate(rectangles):
    # Create lists containing all x, y values to determine min and max vals
    x_coordinates, y_coordinates = [], []
    for rectangle in rectangles:
        x_coordinates.append(rectangle[0])
        x_coordinates.append(rectangle[2])
        y_coordinates.append(rectangle[1])
        y_coordinates.append(rectangle[3])
    x_min, x_max = min(x_coordinates), max(x_coordinates)
    y_min, y_max = min(y_coordinates), max(y_coordinates)
    x, y = x_min, y_min
    area_total = 0
    while x < x_max:
        while y < y_max:
            if (x, y) in rectangles:
                pass






