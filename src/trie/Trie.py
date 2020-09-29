from .TrieNode import TrieNode


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
            '[': 38,
            '!': 39
        }
        c = c.lower()

        if c.isalpha():
            return ord(c) - ord('a')

        elif c in other_char:
            return other_char[c]

        else:
            return -1

    def insert(self, word, node=None):
        crawler = self.root if not node else node

        for i, c in enumerate(word):
            index = self._char_to_index(c)
            if not crawler.children[index]:
                crawler.children[index] = self.get_node()

            if c == 'a':
                temp = word[(i+1):]
                self.insert('4'+temp, crawler)
                self.insert('@'+temp, crawler)

            if c == 'c':
                temp = word[(i+1):]
                self.insert('('+temp, crawler)
                self.insert('[' + temp, crawler)

            if c == 'e':
                temp = word[(i+1):]
                self.insert('3'+temp, crawler)

            if c == 'g':
                temp = word[(i+1):]
                self.insert('6'+temp, crawler)

            if c == 'i':
                temp = word[(i+1):]
                self.insert('|'+temp, crawler)
                self.insert('!'+temp, crawler)

            if c == 'j':
                temp = word[(i+1):]
                self.insert(']'+temp, crawler)

            if c == 'l':
                temp = word[(i+1):]
                self.insert('1'+temp, crawler)

            if c == 'o':
                temp = word[(i+1):]
                self.insert('0'+temp, crawler)

            if c == 's':
                temp = word[(i+1):]
                self.insert('5'+temp, crawler)
                self.insert('$'+temp, crawler)

            if c == 't':
                temp = word[(i+1):]
                self.insert('7'+temp, crawler)

            if c == 'z':
                temp = word[(i+1):]
                self.insert('2'+temp, crawler)

            crawler = crawler.children[index]

        crawler.is_end_of_word = True


    def search(self, word):
        crawler = self.root
        length = len(word)

        for char in word:
            index = self._char_to_index(char)
            if not crawler.children[index]:
                print("Char not found: " + char)
                return False
            crawler = crawler.children[index]

        return crawler is not None and crawler.is_end_of_word