from models.node_model import NodeModel
from math import *


def are_coordinates_on_node(node: NodeModel, x: int, y: int) -> bool:
    dx = abs(x - node.x_coord)
    dy = abs(y - node.y_coord)

    if (dx + dy <= node.radius) or (
            pow(dx, 2) + pow(dy, 2) <= pow(node.radius, 2)):  # if click is inside circle or on the contour
        return True
    else:
        return False


def get_middle_point_of_line(start_node: NodeModel, end_node: NodeModel) -> tuple:
    middle_point_x = int((start_node.x_coord + end_node.x_coord) / 2)
    middle_point_y = int((start_node.y_coord + end_node.y_coord) / 2)

    return (middle_point_x, middle_point_y)


def get_valid_number(entry_input: str) -> int:
    default_number = 0
    if entry_input is None:
        return default_number
    elif entry_input.isdigit():
        default_number = int(entry_input)

    return default_number

