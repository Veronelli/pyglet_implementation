def sum_difference(a: int, b: int) -> int:
    """
    Calculate the sum of the maximum of two integers and their absolute difference.
    Args:
        a (int): The first integer.
        b (int): The second integer.
    Returns:
        int: The sum of the maximum of the two integers and their absolute difference.
    """

    difference = abs(a - b)
    if difference > 0:
        return max(a, b) + difference
    return a