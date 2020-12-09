class HuffmanNode:
    def __init__(self, byte=None, freq: int = 0, left=None, right=None):
        self.byte = byte
        self.freq = freq

        self.left = left
        self.right = right

    def __lt__(self, other) -> bool:
        return self.freq < other.freq

    def is_leaf(self) -> bool:
        return self.left is None and self.right is None
