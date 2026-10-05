# ASSIGNMENT 1 - DSA  T Jeevantej BSDBG2519
# BINOMIAL HEAP

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = None
        self.left = None
        self.right = None

# Utility function: Link two binomial trees

def link_tree(root1, root2):
    if root1.value > root2.value:
        root1, root2 = root2, root1

    root2.parent = root1
    root2.right = root1.left
    root1.left = root2
    root1.rank += 1

    return root1

# Find a root of a particular rank

def add_tree(table, tree):
    current = tree

    while True:
        r = current.rank

        if table[r] is None:
            table[r] = current
            return

        current = link_tree(table[r], current)
        table[r] = None

# 1. BUILD HEAP

def build_heap(values):
    heap = []

    for value in values:
        heap = insert(heap, value)

    return heap

# 2. INSERT

def insert(heap, value):
    new_tree = Node(value)

    all_roots = heap + [new_tree]

    max_rank = len(all_roots) + 2
    table = [None] * max_rank

    for tree in all_roots:
        tree.parent = None
        tree.right = None
        add_tree(table, tree)

    new_heap = []

    for tree in table:
        if tree is not None:
            tree.right = None
            new_heap.append(tree)

    return new_heap

# Display Heap

def display(heap):
    if not heap:
        print("Heap is empty")
        return

    for tree in heap:
        print("B" + str(tree.rank) + ":", tree.value)

# 3. FIND MINIMUM

def find_minimum(heap):
    if not heap:
        return None

    minimum = heap[0].value

    for tree in heap:
        if tree.value < minimum:
            minimum = tree.value

    return minimum

# 4. EXTRACT MINIMUM

def extract_minimum(heap):

    if not heap:
        return [], None

    min_index = 0

    for i in range(1, len(heap)):
        if heap[i].value < heap[min_index].value:
            min_index = i

    minimum_tree = heap[min_index]

    remaining = heap[:min_index] + heap[min_index + 1:]

    children = []
    child = minimum_tree.left

    while child is not None:
        next_child = child.right

        child.parent = None
        child.right = None

        children.append(child)
        child = next_child

    combined = remaining + children

    if not combined:
        return [], minimum_tree.value

    table = [None] * (len(combined) + 3)

    for tree in combined:
        add_tree(table, tree)

    result = []

    for tree in table:
        if tree is not None:
            tree.right = None
            result.append(tree)

    return result, minimum_tree.value

# 5. UNION OF TWO HEAPS

def union(heap1, heap2):

    combined = heap1 + heap2

    if not combined:
        return []

    table = [None] * (len(combined) + 3)

    for tree in combined:
        tree.parent = None
        tree.right = None
        add_tree(table, tree)

    result = []

    for tree in table:
        if tree is not None:
            tree.right = None
            result.append(tree)

    return result

# 6. DECREASE KEY

def decrease_key(node, new_value):

    if new_value > node.value:
        return False

    node.value = new_value

    current = node

    while current.parent is not None:

        parent = current.parent

        if current.value >= parent.value:
            break

        current.value, parent.value = parent.value, current.value

        current = parent

    return True

# Search for a node

def search_node(root, value):

    if root is None:
        return None

    if root.value == value:
        return root

    child = root.left

    while child is not None:

        result = search_node(child, value)

        if result is not None:
            return result

        child = child.right

    return None


def find_node(heap, value):

    for tree in heap:

        result = search_node(tree, value)

        if result is not None:
            return result

    return None

# 7. DELETE A NODE

def delete_node(heap, value):

    node = find_node(heap, value)

    if node is None:
        return heap, False

    decrease_key(node, float("-inf"))

    heap, removed = extract_minimum(heap)

    return heap, True

# EXAMPLE

values = [36, 9, 27, 54, 18, 45, 7]

heap = build_heap(values)

print("Initial Binomial Heap:")
display(heap)

print("\nMinimum element:")
print(find_minimum(heap))

heap, minimum = extract_minimum(heap)

print("\nAfter Extract Minimum:")
print("Removed:", minimum)
display(heap)

heap = insert(heap, 3)

print("\nAfter Inserting 3:")
display(heap)

print("\nMinimum element:")
print(find_minimum(heap))