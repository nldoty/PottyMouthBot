class TrieNode:
    _MAX_SIZE = 40

    def __init__(self):
        self.children = [None] * self._MAX_SIZE
        self.is_end_of_word = False

