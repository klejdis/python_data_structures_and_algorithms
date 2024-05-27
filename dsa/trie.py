"""
Trie
- A trie is a tree-like data structure whose nodes store the letters of an alphabet.
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def print(self):
        return self._print(self.root)

    def _print(self, node: TrieNode, level=0, prefix=""):
        if node.end is True:
            return ""

        to_print = ""

        for ch in node.children.keys():
            to_print += "|" + "-" * level + prefix + ch + '\n'
            to_print += self._print(node.children[ch], level + 1, prefix="")
        return to_print

    def insert(self, word: str):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.end = True

    def search(self, word):
        current = self.root
        for ch in word:
            node = current.children.get(ch)
            if node is None:
                return False
            current = node

        return current.end is True

    def delete(self, word):
        self._delete(self.root, word, 0)

    def _delete(self, node, word, index):
        if index == len(word):
            if node.end is False:
                return False
            node.end = False
            return len(node.children) == 0

        ch = word[index]
        child = node.children.get(ch)
        if child is None:
            return False

        should_delete = self._delete(child, word, index + 1)
        if should_delete:
            del node.children[ch]
            return len(node.children) == 0
        return False


if __name__ == "__main__":
    trie = Trie()
    trie.insert('a')

    trie.delete('a')
    print(trie.print())
