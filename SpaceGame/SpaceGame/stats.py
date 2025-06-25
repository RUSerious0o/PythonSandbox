class Stats():
    """остлеживание статистики"""

    def __init__(self):
        """инициализирует статистику"""
        self.guns_left = 0
        self.reset_stats()
        self.run_game = True
        with open('high_score.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """статистика, извемянющаяся во время игры"""
        self.guns_left = 2
        self.score = 0
