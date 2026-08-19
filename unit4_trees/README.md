# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

---

## Completed Implementation

> The original requirement prompts above are preserved for reference. The code
> in `unit4_discussion.py` was completed to satisfy each of them.

### Design Approach: An Employee-ID Registry as a BST

I implemented a Binary Search Tree to organize employee records keyed by their ID
number, matching the assignment's real-world scenario. Each `Node` stored a value
plus `left` and `right` child references, and the `BST` class kept a reference to
the `root`.

- `insert(value)` delegated to `_insert_recursive`, which created a new `Node` when
  it reached an empty slot. It placed smaller values in the `left` subtree and
  larger values in the `right` subtree, and it ignored duplicates so each employee
  ID appeared exactly once.
- `search(value)` delegated to `_search_recursive`, returning `True` when the value
  matched and `False` at an empty slot. Because each comparison sent the search into
  only one subtree, it discarded roughly half of the remaining nodes at every step.
- `inorder()` returned the values from a left-current-right traversal. Since the
  left subtree always holds smaller values and the right subtree larger ones, this
  produced the employee IDs in sorted order.

In the demo I inserted seven IDs in a balanced order (middle value first, then the
halves, then the quarters) so the tree stayed shallow. The in-order traversal
printed them sorted, and searches for two existing and two missing IDs behaved as
expected.

### Edge Cases Handled

I tested an empty tree (in-order traversal returned `[]` and search returned
`False`), a duplicate insertion (changed nothing, so the tree kept one copy of the
key), and a single-node tree (search and traversal worked normally).

### How Trees Improve Performance, and Why BSTs Can Become Inefficient

A balanced BST improves on linear structures: a search halves the search space at
each level, so lookups take O(log n) on average instead of the O(n) of a linear scan
through a list. In-order traversal also yields sorted output in O(n) without a
separate sort.

However, the shape of the tree depends entirely on insertion order. If IDs are
inserted sequentially (1001, 1002, 1003, ...), every new value is larger than the
root and always descends the right branch, so the tree degenerates into a
linked-list shape with height n. Searches then visit every node, degrading to O(n)
and erasing the BST's advantage. I demonstrated this by counting the nodes visited:
the balanced tree needed about 3 comparisons for seven IDs, while the sequential
tree needed all 8. This is why self-balancing variants (AVL or red-black trees)
rebalance after each insert to keep the height near O(log n).

### Memory Usage

The BST stores exactly one node per unique value, so memory grows in O(n) as
records are added. Each node holds the value plus two child pointers, adding a small
fixed overhead per element compared with a flat list.

### Discussion Board Reflection

While completing this assignment I learned how recursion drives the core BST
operations of insertion, search, and in-order traversal. I also learned that the
same set of values can produce very different tree shapes depending on insertion
order, which directly controls how fast searches run.

The main challenge was tracking the recursion and making sure each subtree returned
its updated root so the parent links stayed correct. I overcame this by having the
recursive helpers return the node reference at every level and storing the result
back into the child pointer.

Compared with other data structures, a BST offers a good balance: faster than a
linear search for ordered lookups and dynamic inserts, and it gives sorted output
for free. Its weakness is that unbalanced input order can turn it into a linked
list, which is why self-balancing trees exist to keep performance consistent.