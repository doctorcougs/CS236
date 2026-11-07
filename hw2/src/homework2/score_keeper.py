class ScoreKeeper:
    def __init__(self) -> None:
        self.multiplier = 1  # used in calculation
        self.total_score = 0  # altered in method

    def add_points(self, points: int) -> int:
        """
        Add points multiplied by self.multiplier to total_score.
        Return the amount of points added in this call.
        """
        added_points = points * self.multiplier
        self.total_score += added_points
        return added_points
