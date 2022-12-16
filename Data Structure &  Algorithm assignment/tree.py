class TreeNode(object):
    """Node of a Tree"""

    def __init__(self, name='root', children=None, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)

    def __repr__(self):
        return self.name

    def depth(self):  # Depth of current node
        if self.is_root():
            return 0
        else:
            return 1 + self.parent.depth()

    def add_child(self, node):
        node.parent = self
        assert isinstance(node, TreeNode)
        self.children.append(node)

    def remove_parent(self):
        node = self
        parent = node.parent
        for x in parent.children:
            if str(x) == str(node.name):
                parent.children.remove(x)


class Tree:
    """
    Tree implementation as a collection of TreeNode objects
    """

    def __init__(self):
        self.root = None
        self.height = 0
        self.nodes = []
        self.typeOfTraversal = 'DFS'

    def insert(self, node, parent):  # Insert a node into tree
        if parent is not None:
            parent.add_child(node)
        else:
            if self.root is None:
                self.root = node
        self.nodes.append(node)

    def getNodeByLevel(self, level):
        listOfnodes = []
        for x in self.nodes:
            if x.depth() == level:
                listOfnodes.append(x.name)
        return listOfnodes

    def contains(self, node):
        if node in self.nodes:
            return True
        return False

    def delete(self, node):
        node.remove_parent()
        self.nodes.remove(node)



    @staticmethod
    def BreadthFirstTraversal(starting_node):
        queue = [starting_node]
        traversal_list = [starting_node]
        while queue:
            current_node = queue.pop(0)
            for i in current_node.children:
                traversal_list.append(i)
                queue.append(i)
        return traversal_list

    @staticmethod
    def DepthFirstTraversal(starting_node, path=[]):
        path.append(starting_node)
        if len(starting_node.children) == 0:
            return None
        else:
            for next_node in starting_node.children:
                Tree.DepthFirstTraversal(next_node, path)
            if starting_node not in path:
                path.append(starting_node)
            return path

    def __iter__(self):
        if self.typeOfTraversal == 'DFS':
            dfs_traversal_list = Tree.DepthFirstTraversal(self.root)
            for x in dfs_traversal_list:
                yield x
        elif self.typeOfTraversal == 'BFS':
            bfs_traversal_list = Tree.BreadthFirstTraversal(self.root)
            for x in bfs_traversal_list:
                yield x
        else:
            raise ValueError('Invalid traversal type')

    def __call__(self, traversal_type):
        self.typeOfTraversal = traversal_type
        return self

    def __str__(self):
        output = ''
        for x in self.__iter__():
            output += str(x) + '-->'
        return output


if __name__ == "__main__":
    root = TreeNode('GrandPa')
    tree = Tree()
    tree.insert(root, None)
    a = TreeNode('Boy1')
    b = TreeNode('Boy2')
    c = TreeNode('Boy3')
    d = TreeNode('Boy4')
    e = TreeNode('Boy5')
    tree.insert(a, root)
    tree.insert(b, root)
    tree.insert(c, root)
    tree.insert(d, root)
    tree.insert(e, root)
    c1 = TreeNode('child1')
    c2 = TreeNode('child2')
    c3 = TreeNode('child3')
    c4 = TreeNode('child4')
    c5 = TreeNode('child5')
    c6 = TreeNode('child6')
    c7 = TreeNode('child7')
    c8 = TreeNode('child8')
    c9 = TreeNode('child9')
    c10 = TreeNode('child0')
    tree.insert(c1, a)
    tree.insert(c2, a)
    tree.insert(c3, b)
    tree.insert(c4, b)
    tree.insert(c5, c)
    tree.insert(c6, c)
    tree.insert(c7, d)
    tree.insert(c8, d)
    tree.insert(c9, e)
    tree.insert(c10, e)
    print(tree.nodes)
    print(f"depth of root is:{c10.depth()}")
    print(tree.getNodeByLevel(2))
    # tree.delete(c10)
    # print(c1.parent)
    # # print(tree.nodes)
    # for x in tree:
    #     print(x)

    print(tree)


