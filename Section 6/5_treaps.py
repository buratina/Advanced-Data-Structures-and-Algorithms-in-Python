from random import randint


class Node:

    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None


def search(node, key):
    if not node:
        return False
    if node.key == key:
        return True

    if key < node.key:
        return search(node.left, key)
    return search(node.right, key)


def inorder(node):
    if not node:
        return ', '

    left = inorder(node.left)
    inner = str(node.key)
    right = inorder(node.right)

    return left + inner + right


def rotate_left(node):
    rotated = node.right
    node.right = rotated.left
    rotated.left = node
    return rotated


def rotate_right(node):
    rotated = node.left
    node.left = rotated.right
    rotated.right = node
    return rotated


def balance_tree(node):
    if node.left and node.left.priority < node.priority:
        return rotate_right(node)
    elif node.right and node.right.priority < node.priority:
        return rotate_left(node)
    return node


def insert(node, key):
    if not node:
        return Node(key, randint(1, 10000))

    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return balance_tree(node)


def remove(node, key):
    if not node:
        return node
    if node.key == key:
        return None

    if key < node.key:
        node.left = remove(node.left, key)
    else:
        node.right = remove(node.right, key)
    return balance_tree(node)


python_set = set()
treap = None
for i in range(10000):

    op = randint(1, 3)
    if op == 1:
        val = randint(1, 1000)
        print('Searching {}\npython set={}\nour treap={}\n'.format(
            val,
            sorted(python_set),
            inorder(treap)))
        assert (val in python_set) == search(treap, val),\
            'mismatch in search, set={}, treap={} value={}'.format(
                val in python_set,
                search(treap, val),
                val
            )
    elif op == 2:
        val = randint(1, 1000)
        print('Adding {}\npython set={}\nour treap={}\n'.format(
            val,
            sorted(python_set),
            inorder(treap)))
        python_set.add(val)
        if not search(treap, val):
            treap = insert(treap, val)
    else:
        val = randint(1, 1000)
        print('Removing {}\npython set={}\nour treap={}\n'.format(
            val,
            sorted(python_set),
            inorder(treap)))
        if val in python_set:
            python_set.remove(val)
        treap = remove(treap, val)


