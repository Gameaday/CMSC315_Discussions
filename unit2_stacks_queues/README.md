# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

---

## Completed Implementation

> The original requirement prompts above are preserved for reference. The code
> in `unit2_discussion.py` was completed to satisfy each of them.

### Stack (LIFO) — Text Editor "Undo" History

I implemented the `Stack` class using a Python list. A list stores items in order
and lets us add to and remove from the end in O(1) time, which represents the "top"
of the stack.

- `push(value)` appended the new action to the **end** of the list, making it the
  most recent item. Because the newest item is the first one later removed, this
  produced **LIFO (Last-In, First-Out)** behavior.
- `pop()` removed and returned the last (most recent) item. If the stack was
  empty, it printed a warning and returned `None` instead of crashing.
- `peek()` returned the top item **without removing it**, acting as a "look,
  don't touch" read of the most recent action.
- `is_empty()` returned `True` when the list held no items.

I modeled the demo on a text editor's Undo history: each editing action was pushed
onto the stack, and Undoing popped the most recent action first. Edge cases were
tested by popping and peeking an empty stack, and by confirming a single-item stack
became empty after its one item was removed.

### Queue (FIFO) — Coffee Shop Customer Line

I implemented the `Queue` class using `collections.deque`, a double-ended queue
that supports O(1) append at the back and O(1) removal at the front.

- `enqueue(value)` appended the new value to the **back** of the line, so earlier
  arrivals (already at the front) were still served first. This produced **FIFO
  (First-In, First-Out)** behavior.
- `dequeue()` removed and returned the front (earliest arrival) item. If the queue
  was empty, it printed a warning and returned `None` instead of crashing.
- `front()` returned the front item **without removing it**, showing who was next
  in line.
- `is_empty()` returned `True` when the deque held no items.

I modeled the demo on a coffee shop customer line: customers joined at the back and
were served in arrival order. Edge cases were tested by dequeuing and viewing the
front of an empty queue, and by confirming a single-item queue became empty after
its one item was removed.

### Memory Usage

Both structures grew proportionally to the number of items stored. The stack stored
each added value once in its list, and the queue stored each added value once in its
deque, so total memory grew in **O(n)** as n items were added. When items were
removed, that slot was freed, so memory did not grow beyond the structures' contents.

### Discussion Board Reflection

While completing this assignment I learned how to implement and analyze two
fundamental container structures: a stack and a queue. I learned that the key
difference is governed solely by *where* items are inserted and removed. The stack
adds and removes at the same end, so the most recent item is handled first (LIFO),
while the queue adds at one end and removes at the other, so the earliest item is
handled first (FIFO).

The main challenge I faced was deciding how to handle operations on empty
structures. I chose to return `None` with a printed warning rather than raising an
exception, which kept the demo running and made the edge case visible. I also used a
`deque` rather than a plain list for the queue because removing from the front of a
list is O(n), whereas `popleft()` on a deque is O(1).

In the real world, a stack maps naturally to an Undo history or the back-button in a
browser (last visited page returned first), while a queue maps to a customer line or
a printer's job queue (first job submitted printed first). Understanding which order
to use lets software behave predictably and feel responsive.

