class Node:
    def __init__(self):
        self.children = {}
        self.flag = False

class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        currentNode = self.root

        for letter in word:
            if letter not in currentNode.children:
                currentNode.children[letter] = Node()
            currentNode = currentNode.children[letter]

        currentNode.flag = True
        return True

    def search(self, word):
        currentNode = self.root

        for letter in word:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]
        
        if currentNode.flag:
            return True
        else:
            return False

    def startsWith(self, prefix):
        currentNode = self.root

        for letter in prefix:
            if letter not in currentNode.children:
                return False
            currentNode = currentNode.children[letter]

        return True

    def __str__(self, node=None, currentText=""):
        if node is None: node = self.root
        self.traverse(node, currentText)
        return ""

    def traverse(self, node, currentText):
        for char, nextNode in node.children.items():
            nextChar = currentText + char

            if nextNode.flag:
                print(nextChar)
            self.traverse(nextNode, nextChar)
            

trie = Trie()
trie.add("hello")
trie.add("hel")
trie.add("apple")
print(trie.startsWith("applee"))
print(trie)