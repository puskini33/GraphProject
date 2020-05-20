from models.node_model import NodeModel


def are_coordinates_on_node(node: NodeModel, x: int, y: int) -> bool:
    dx = abs(x - node.x_coord)
    dy = abs(y - node.y_coord)

    if (dx + dy <= node.radius) or (
            pow(dx, 2) + pow(dy, 2) <= pow(node.radius, 2)):  # if click is inside circle or on the contour
        return True
    else:
        return False
