class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def in_order_traversal(self, node):
        result = []
        self._in_order_traversal(node, result)
        return result

    def _in_order_traversal(self, node, result):
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.key)
            self._in_order_traversal(node.right, result)

    def pre_order_traversal(self, node):
        result = []
        self._pre_order_traversal(node, result)
        return result

    def _pre_order_traversal(self, node, result):
        if node:
            result.append(node.key)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)

    def post_order_traversal(self, node):
        result = []
        self._post_order_traversal(node, result)
        return result

    def _post_order_traversal(self, node, result):
        if node:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.key)

    def level_order_traversal(self, node):
        result = []
        if node is None:
            return result

        queue = [node]
        while queue:
            current = queue.pop(0)
            result.append(current.key)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return result

# Example Usage
if __name__ == "__main__":
    tree = BinaryTree()
    nodes = [10, 5, 15, 3, 7, 12, 18]
    for node in nodes:
        tree.insert(node)

    print("In-order traversal:", tree.in_order_traversal(tree.root))
    print("Pre-order traversal:", tree.pre_order_traversal(tree.root))
    print("Post-order traversal:", tree.post_order_traversal(tree.root))
    print("Level-order traversal:", tree.level_order_traversal(tree.root))


friends = [
    ["Quan", ["Thao"]],
    ["Thao", "Tung"],
    ["Hieu", "Tai"],
    ["Hieu", "Viet"],
    ["Minh", "Suong"]
]