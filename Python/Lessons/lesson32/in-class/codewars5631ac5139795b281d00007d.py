# Urban Dictionary
# https://www.codewars.com/kata/5631ac5139795b281d00007d

# 1
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if i == len(word):
                return node.is_end_of_word
            ch = word[i]
            if ch == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            if ch not in node.children:
                return False
            return dfs(node.children[ch], i + 1)

        return dfs(self.root, 0)


# 2
# from collections import defaultdict
# import re
#
# class WordDictionary:
#     def __init__(self):
#         self.words = defaultdict(set)
#
#     def add_word(self, word: str) -> None:
#         self.words[len(word)].add(word)
#
#     def search(self, word: str) -> bool:
#         n = len(word)
#         if n not in self.words:
#             return False
#         if '.' not in word:
#             return word in self.words[n]
#         pattern = '^' + re.escape(word).replace(r'\.', '.') + '$'
#         return any(re.fullmatch(pattern, w) for w in self.words[n])


if __name__ == "__main__":
    wd = WordDictionary()
    wd.add_word("a")
    wd.add_word("at")
    wd.add_word("ate")
    wd.add_word("ear")

    assert wd.search("a") is True
    assert wd.search("a.") is True
    assert wd.search("a.e") is True
    assert wd.search("b") is False
    assert wd.search("e.") is False
    assert wd.search("ea.") is True
    assert wd.search("ea..") is False

    wd.add_word("co")
    wd.add_word("cod")
    wd.add_word("code")
    wd.add_word("codewars")

    assert wd.search("........") is True
    assert wd.search("c.o") is False
    assert wd.search("cod.") is True
    assert wd.search("c.o") is False
    assert wd.search("co..w..s") is True
    assert wd.search("co..w..") is False

    print("All tests passed")