class Trie:

    def __init__(self):
        self.tree = {}
        
    def insert(self, word: str) -> None:
        tree = self.tree
        for letter in word:
            if letter not in tree:
                tree[letter] = {}
            
            tree = tree[letter]
        
        tree["0"] = 0
        
        
    def search(self, word: str) -> bool:
        tree = self.tree
        is_search = True
        for letter in word:
            if letter not in tree:
                is_search = False
                break
            
            tree = tree[letter]
            
        is_search = is_search and ("0" in tree)
            
        return is_search
            
    def startsWith(self, prefix: str) -> bool:
        tree = self.tree
        is_start = True
        for letter in prefix:
            if letter not in tree:
                is_start = False
                break
            
            tree = tree[letter]
            
        return is_start


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)