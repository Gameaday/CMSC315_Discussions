"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # Each BST node holds one value plus up to two child references.
        # By BST rules, left holds smaller values and right holds larger ones.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # A new tree starts with no nodes; the root is None until the first
        # value is inserted.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Public entry point: delegate to the recursive helper, starting at the
        # root. The helper returns the (possibly new) subtree root, which we
        # store back so the tree is always kept up to date.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: we found the empty slot where the value belongs, so this
        # becomes a new leaf node.
        if node is None:
            return Node(value)
        # The whole point of a BST: smaller values must live in the LEFT subtree
        # and larger values in the RIGHT subtree. Comparing each step tells us
        # which half to descend into, so we never need to search the other half.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If value == node.value we do nothing: duplicates are ignored so the
        # tree keeps a single copy of each key.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Public entry point that delegates to the recursive helper from root.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Reached an empty slot without finding the value -> not present.
        if node is None:
            return False
        # Found it.
        if value == node.value:
            return True
        # Descend into only ONE branch per step. Because left holds smaller
        # values and right holds larger values, each comparison discards half
        # the remaining search space. On a balanced tree this is O(log n) vs
        # O(n) for a linear scan through a list.
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Start an empty list and fill it via the recursive helper.
        return self._inorder_recursive(self.root, [])

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Base case: nothing here, so return the list as-is.
        if node is None:
            return values
        # In-order = left, current, right. Because every left value is smaller
        # than the node and every right value is larger, visiting left-first
        # then the node then the right yields the values in sorted order.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)
        return values


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION: Employee Records by ID ===")

    # Scenario: an HR app stores employee records keyed by their ID number.
    # We insert IDs in a "balanced" order - the middle value first, then the
    # halves, then the quarters - so the tree stays shallow and searches stay fast.
    emp_tree = BST()
    balanced_ids = [1050, 1025, 1075, 1012, 1037, 1062, 1087]
    print(f"Inserting employee IDs in BALANCED order: {balanced_ids}")
    for emp_id in balanced_ids:
        emp_tree.insert(emp_id)

    # At each insert, comparing the new ID to the current node sends it into
    # only one half (left = smaller, right = larger). Because the root (1050)
    # splits the range in half, and each level splits again, every search
    # discards ~half the remaining space -> O(log n) comparisons on this tree.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print(f"Employee IDs in sorted order: {emp_tree.inorder()}")
    # In-order visits left, then current, then right. Since the left subtree
    # always holds smaller IDs and the right subtree larger ones, the traversal
    # naturally lists every employee ID in ascending order - like a sorted index.

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    # Values that exist: each comparison halves the search space until found.
    for emp_id in (1025, 1087):
        print(f"Employee {emp_id} exists? {emp_tree.search(emp_id)}")
    # Values that do not exist: search reaches an empty slot and returns False.
    for emp_id in (1099, 1001):
        print(f"Employee {emp_id} exists? {emp_tree.search(emp_id)}")
    # Notice the searches do not scan every record - on the balanced tree each
    # lookup checks at most ~log2(7) ~ 3 nodes, far fewer than a linear search.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge 1: empty tree. Traversal returns [] and search returns False safely.
    empty = BST()
    print(f"Empty tree in-order traversal -> {empty.inorder()}")
    print(f"Search in an empty tree (ID 1001) -> {empty.search(1001)}")

    # Edge 2: duplicate insertion. Inserting 1050 again changes nothing, so the
    # tree keeps exactly one copy of each employee ID.
    before = emp_tree.inorder()
    emp_tree.insert(1050)
    print(f"\nDuplicate insert of 1050 changes tree? {emp_tree.inorder() != before} (tree stays: {emp_tree.inorder()})")

    # Edge 3: single-node tree works like a normal BST (root is the one node).
    single = BST()
    single.insert(2024)
    print(f"Single-node tree: contains 2024? {single.search(2024)}, in-order -> {single.inorder()}")

    # ===============================
    # INSERTION-ORDER COMPARISON (assignment's key point)
    # ===============================
    # The same IDs added in SEQUENTIAL order (1001, 1002, ...) create a skewed
    # tree shaped like a linked list: every new ID is larger, so it always
    # descends the right branch. Searches then check every node -> O(n),
    # losing the BST's efficiency advantage. We just count nodes visited to show
    # the difference in depth (a balanced tree visits ~log2(n), the skewed one
    # visits all n).
    skewed = BST()
    for emp_id in range(1001, 1009):      # 1001..1008 added in increasing order
        skewed.insert(emp_id)

    # Count how many nodes a search must visit: the path length from root.
    def path_length(node, target, steps):
        if node is None or node.value == target:
            return steps + 1
        if target < node.value:
            return path_length(node.left, target, steps + 1)
        return path_length(node.right, target, steps + 1)

    balanced_steps = path_length(emp_tree.root, 1087, 0)
    skewed_steps = path_length(skewed.root, 1008, 0)
    print(f"\n=== INSERTION ORDER MATTERS ===")
    print(f"Searching last ID in balanced tree (7 IDs): visits ~{balanced_steps} node(s).")
    print(f"Searching last ID in sequential tree (8 IDs): visits {skewed_steps} node(s) - like a linked list!")
    print("Conclusion: inserting in sequential order skews the tree and degrades "
          "searches to O(n); a balanced insertion order keeps them near O(log n).")


if __name__ == "__main__":
    main()