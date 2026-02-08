class Colors:
    """TETRIS colors"""
    TETRIS_COLORS = {
    "-":(26, 31, 40), # Empty
    "I": (0, 255, 255),   # Cyan
    "O": (255, 255, 0),   # Yellow
    "T": (160, 0, 240),   # Purple
    "S": (0, 255, 0),     # Green
    "Z": (255, 0, 0),     # Red
    "J": (0, 0, 255),     # Blue
    "L": (255, 165, 0),   # Orange
    }

    @classmethod
    def get_block_colors(cls):
        return list(cls.TETRIS_COLORS.values())

