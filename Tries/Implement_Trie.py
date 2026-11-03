#clarify: insert -> insert word as a set of its letters each consecutive letter being a child. "Mark" last letter
#edge cases -> last letter can it just be the null or should i add another part to the node marking it as the end. Add empty string cases

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

#go down existing sections of the word until you find a letter that hasnt been included
#then start adding the remaining letters
#pseudocode:
#for letter in word:
    #start at root:
        #if letter child or root move on to its child
        #else creating a child from curr root to this new letter
    def insert(self, word: str) -> None:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            else:
                curr = curr.children[letter]
        #curr = curr.children[word[-1]]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for letter in word:
            if letter not in curr.children:
                return False
            else:
                curr = curr.children[letter]
        if curr.endOfWord:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for letter in prefix:
            if letter not in curr.children:
                return False
            else:
                curr = curr.children[letter]
        return True
