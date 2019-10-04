import sys

sys.setrecursionlimit(4000)


class Node:
    def __init__(self, data: int, left: "Node" = None, right: "Node" = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def is_leaf(self):
        return self.right is None and self.left is None


class BST:
    def __init__(self, root: Node) -> None:
        self.root = root

    def pre_order_traversal(self, root: Node) -> None:
        if root is None:
            return
        print(root.data, end=' ')
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def post_order_traversal(self, root: Node) -> None:
        if root is None:
            return
        self.post_order_traversal(root.left)
        self.post_order_traversal(root.right)
        print(root.data, end=' ')

    def g(self, root: Node) -> [int, int]:
        if root.is_leaf():
            return root.data, root.data

        f_left, max_left = self.g(root.left)
        f_right, max_right = self.g(root.right)

        f_root = root.data + max(f_left, f_right, max_left + max_right)
        max_root = root.data + max(max_left, max_right)
        return f_root, max_root

    @staticmethod
    def create_bst_from_pre_post(pre: list, post: list) -> "BST":
        if len(pre) == 1 and len(post) == 1:
            return BST(Node(pre[0]))
        tree = BST(Node(pre[0]))
        left = pre[1]
        right = post[-2]
        tree.root.left = BST.create_bst_from_pre_post(pre[1:pre.index(right)], post[:post.index(left)+1]).root
        tree.root.right = BST.create_bst_from_pre_post(pre[pre.index(right):], post[post.index(left)+1:-1]).root
        return tree


for _ in range(int(input())):
    pre = list(map(int, input().replace('pre: ', '').replace(',', '').split(' ')))
    post = list(map(int, input().replace('post: ', '').replace(',', '').split(' ')))
    tree = BST.create_bst_from_pre_post(pre, post)
    print(tree.g(tree.root)[0])
