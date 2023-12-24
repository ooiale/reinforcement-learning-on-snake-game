def is_closed_shape(coordinates):
    # Ensure that the list contains at least three coordinates
    if len(coordinates) < 3:
        return False

    # Calculate the signed area using the Shoelace formula
    area = 0.5 * sum((x0 * y1 - x1 * y0) for (x0, y0), (x1, y1) in zip(coordinates, coordinates[1:] + [coordinates[0]]))

    # Check if the signed area is non-zero, indicating a closed shape
    return abs(area) > 0


if __name__ == '__main__':
    # Example usage:
    coordinates_list = [(0, 0), (1, 0), (2, 0), (3, 0),(3,1), (3,2),(2,3),(1,3),(1,2)]
    result = is_closed_shape(coordinates_list)
    print(result)
