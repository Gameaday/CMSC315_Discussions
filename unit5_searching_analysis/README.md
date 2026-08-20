# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

---

## Completed Implementation

> The original requirement prompts above are preserved for reference. The code
> in `unit5_discussion.py` was completed to satisfy each of them.

### Design Approach: Finding a Song in a Streaming Catalog

I implemented linear and binary search and demonstrated them on a music streaming
catalog keyed by song IDs, mirroring how a user searches for a track in a library.

- `linear_search(lst, target)` scanned the list from the first element to the last
  using `enumerate()`, returning the index of the first match or `-1`. It needs no
  particular ordering, but in the worst case it examines every element, giving O(n)
  time complexity.
- `binary_search(lst, target)` assumed a sorted list and used two bounds, `low` and
  `high`. Each iteration checked the middle element; based on that comparison it
  kept only the left or right half, discarding the other. This halves the search
  space each step, giving O(log n) time complexity.

In the demo I tested both on a small sorted catalog (found and missing values) and
on a large 10,000-element list. I also wrote small comparison-counting helpers so
the output shows the difference directly: finding the last song took about 10,000
comparisons with linear search but only 14 with binary search.

### Edge Cases Handled

I tested four edge cases: an empty list (both return `-1`), a single-element list
(found and missing), a target at the first position (index 0), and a target at the
last position. All returned the correct index or `-1` without errors.

### Why Binary Search Is Faster, and When Linear Search Is Still Right

Binary search is faster because it halves the remaining search space on every
comparison. For n items that means, at most, about log2(n) steps, whereas linear
search may need all n. This is why the advantage grows dramatically as datasets get
larger.

Linear search still has its place. It is the better choice when the data is small,
unsorted, or when only one or a few lookups are needed, because there is no sorting
preparation cost. For example, searching an unsorted list of a few dozen contacts
in a small phone directory is fine with linear search. Sorting the data first would
cost O(n log n), which is not worth it for tiny collections or one-off searches.

### When Binary Search Is Not Usable

Binary search cannot be used (or gives incorrect results) when: the data is not
sorted; when the structure does not support O(1) random access by index, such as a
linked list, where repeatedly jumping to the middle requires linear cost; or when
the data changes frequently, since every insert would force a re-sort to keep binary
search valid.

### Memory Usage

Both algorithms are in-place and add no extra memory beyond the input list itself,
using O(1) additional space regardless of dataset size.

### Discussion Board Reflection

While completing this assignment I learned how the same search goal can be solved
with very different cost depending on whether the data is organized. Implementing
both algorithms side by side made the O(n) versus O(log n) difference concrete when
I printed the comparison counts for a 10,000-element list.

The main challenge was correctly narrowing the bounds in binary search so the loop
terminates and does not miss boundary values. I solved this by using `low <= high`
for the loop condition and updating `high = mid - 1` or `low = mid + 1`, which I
verified against targets at the first and last positions.

In real-world terms, binary search shines for large, frequently queried, sorted
datasets such as database indexes and dictionaries, while linear search remains
appropriate for small or unsorted collections and streaming data where random access
is not available. The trade-off is preparation time (sorting) versus search speed.