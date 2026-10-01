"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        closeToOpen = {}

        def dfs(node):
            if node in closeToOpen:
                return closeToOpen[node]


            copy = Node(node.val)

            closeToOpen[node] = copy


            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))


            return copy


        return dfs(node)