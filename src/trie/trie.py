class TrieNode:
    _MAX_SIZE = 38

    def __init__(self):
        self.children = [None] * self._MAX_SIZE
        self.is_end_of_word = False


class Trie:

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()


    def _char_to_index(self, c):
        other_char = {
            '1': 26,
            '2': 27,
            '3': 28,
            '4': 29,
            '5': 30,
            '6': 31,
            '7': 32,
            '0': 33,
            '(': 34,
            '|': 35,
            '@': 36,
            '$': 37,
            '[': 38
        }
        c = c.lower()

        if c.isalpha():
            return ord(c) - ord('a')

        elif c in other_char:
            return other_char[c]

        else:
            return -1

    def insert(self, word):
        crawler = self.root
        length = len(word)
        for i, c in range(length):
            index = self._char_to_index(c)
            if not crawler.children[index]:
                crawler.children[index] = self.get_node()

            if c == 'a':
                word = word[(i+1):]
                self.insert(self, '4'+word)
                self.insert(self, '@'+word)

            if c == 'c':
                word = word[(i+1):]
                self.insert(self, '('+word)
                self.insert(self, '[' + word)

            if c == 'g':
                word = word[(i+1):]
                self.insert(self, '6'+word)

            if c == 'i':
                word = word[(i+1):]
                self.insert(self, '|'+word)

            if c == 'j':
                word = word[(i+1):]
                self.insert(self, ']'+word)

            if c == 'l':
                word = word[(i+1):]
                self.insert(self, 'l'+word)

            if c == 'o':
                word = word[(i+1):]
                self.insert(self, '0'+word)

            if c == 's':
                word = word[(i+1):]
                self.insert(self, '5'+word)

            if c == 't':
                word = word[(i+1):]
                self.insert(self, '7'+word)

            if c == 'z':
                word = word[(i+1):]
                self.insert(self, '2'+word)

            crawler = crawler.children[c]

        crawler.is_end_of_word = True


    def search(self, word):
        crawler = self.root
        length = len(word)

        for char in word:
            index = self._char_to_index(char)
            if not crawler.children[index]:
                return False
            crawler = crawler.children[index]

        return crawler is not None and crawler.is_end_of_word