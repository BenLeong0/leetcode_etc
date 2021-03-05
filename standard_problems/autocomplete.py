words = ['dog','dark','cat','door','dodge']

class Node:
    def __init__(self, children, isWord):
        self.children = children
        self.isWord = isWord

class Solution:
    def build(self, words):
        self.root = Node({}, False)
        for word in words:
            curr = self.root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node(children={}, isWord=False)
                curr = curr.children[char]
            curr.isWord = True
        return

    def autocomplete(self, prefix):
        curr = self.root
        result = []
        for char in prefix:
            if char in curr.children:
                curr = curr.children[char]
            else:
                return result

        def dfs(curr_node=curr, curr_suffix=['']):
            if curr_node.isWord:
                result.append(''.join(curr_suffix))
            for child in curr_node.children:
                dfs(curr_node.children[child],curr_suffix+[child])

        dfs()
        return [prefix + suffix for suffix in result]

s = Solution()
s.build(words)
print(s.autocomplete('do'))
