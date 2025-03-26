class TrieNode():
    def __init__(self):
        self.children = {}
        self.lastNode = False


class Trie(object):

    def __init__(self):
        self.node = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.lastNode = True



    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.node
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.lastNode    

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        cur = self.node
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True     


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)