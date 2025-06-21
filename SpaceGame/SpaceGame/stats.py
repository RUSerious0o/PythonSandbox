class Stats():
    """остлеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.guns_left = 0
        self.reset_stats()

    def reset_stats(self):
        """статистика, извемянющаяся во время игры"""
        self.guns_left = 2
