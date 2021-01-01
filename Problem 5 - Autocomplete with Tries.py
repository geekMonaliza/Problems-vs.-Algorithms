from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False

    def suffixes(self, suffix=''):
        suffixes = []
        for char, node in self.children.items():
            if node.isWord:
                suffixes.append(suffix + char)
            if node.children:
                suffixes += node.suffixes(suffix + char)
        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children[char]
        node.isWord = True

    def exists(self, word):
        node = self.find(word)
        return node.isWord if node else False

    def find(self, prefix):
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)


from ipywidgets import interact

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')

f('f')