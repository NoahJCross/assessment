class Path:
    def __init__(self, distance, is_slope=False, is_paved=True) -> None:
        """
        Initialize a Path object.

        Args:
        - distance: The distance of the path
        - is_slope: A boolean indicating if there's a slope in the path (default is False)
        - is_paved: A boolean indicating if the path is paved (default is True)

        Returns:
        - None
        """
        self.distance = distance
        self.is_slope = is_slope
        self.is_paved = is_paved