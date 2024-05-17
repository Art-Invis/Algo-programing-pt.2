from math import sqrt
from typing import List

def calculate_wire_length(horizontal_distance: float, vertical_distance: float) -> float:
    """
    Calculate the length of the wire needed to span a horizontal and vertical distance.

    Args:
        horizontal_distance (float): The horizontal distance between the two points.
        vertical_distance (float): The vertical distance between the two points.

    Returns:
        float: The length of the wire needed.
    """
    return sqrt(horizontal_distance ** 2 + vertical_distance ** 2)

def validate_input(distance_between_columns: int, column_heights: List[int]) -> bool:
    """
    Validate the input for the distance between columns and the column heights.

    Args:
        distance_between_columns (int): The distance between the columns.
        column_heights (List[int]): The heights of the columns.

    Returns:
        bool: True if input is valid, False otherwise.
    """
    if not (1 <= distance_between_columns <= 100):
        return False
    if not (1 <= len(column_heights) <= 50):
        return False
    if any(height < 1 for height in column_heights):
        return False
    return True

def find_max_wire_length(distance_between_columns: int, column_heights: List[int]) -> float:
    """
    Find the maximum length of wire required to connect the tops or bottoms of the columns.

    Args:
        distance_between_columns (int): The distance between the columns.
        column_heights (List[int]): The heights of the columns.

    Returns:
        float: The maximum wire length required.
    """
    if not validate_input(distance_between_columns, column_heights):
       return None
    
    num_columns = len(column_heights)
    if num_columns == 1:
        return 0  

    max_top_length = 0
    max_bottom_length = 0

    for idx in range(num_columns - 1):
        bottom_to_bottom = distance_between_columns
        height_difference = abs(column_heights[idx] - column_heights[idx + 1])
        max_to_max = calculate_wire_length(distance_between_columns, height_difference)
        one_to_max = calculate_wire_length(distance_between_columns, max(column_heights[idx + 1] - 1, 0))
        max_to_one = calculate_wire_length(distance_between_columns, max(column_heights[idx] - 1, 0))
        
        next_top_length = max(max_to_max + max_top_length, one_to_max + max_bottom_length)
        next_bottom_length = max(max_to_one + max_top_length, bottom_to_bottom + max_bottom_length)

        max_top_length = next_top_length
        max_bottom_length = next_bottom_length

    return round(max(max_top_length, max_bottom_length), 2)
