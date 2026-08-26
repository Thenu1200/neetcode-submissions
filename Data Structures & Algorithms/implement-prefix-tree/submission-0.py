class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] == None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return curr.isLeaf

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            index = ord(letter) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True

        
        