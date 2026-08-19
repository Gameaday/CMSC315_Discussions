"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    # A Stack uses LIFO (Last-In, First-Out): the most recently added value is
    # the first one removed. Think of a pile of plates, or the "Undo" history
    # in a text editor where your newest action is undone first.

    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # A Python list stores items in order and lets us add/remove from the
        # end in O(1) time, which is exactly the "top" of our stack.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Appending to the END of the list places the newest value on top,
        # so it is the next one popped -> this is what makes it LIFO.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Popping an empty stack is an invalid operation, so we return None
        # (and print a warning) instead of crashing the program.
        if self.is_empty():
            print("  [Stack.pop] ERROR: cannot pop an empty stack (returning None).")
            return None
        # list.pop() removes and returns the last item = the top (most recent).
        return self._items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # peek() is a "look, don't touch" read: it returns the top (most recent)
        # value so we can inspect it, but it leaves the stack unchanged.
        if self.is_empty():
            print("  [Stack.peek] ERROR: cannot peek an empty stack (returning None).")
            return None
        return self._items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # True when the list holds no items (length 0).
        return len(self._items) == 0


class Queue:
    # A Queue uses FIFO (First-In, First-Out): the value that arrived first is
    # the one removed first. Think of customers in a coffee shop line or a
    # printer's job queue where people are served in arrival order.

    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        # deque (double-ended queue) supports O(1) append at the back and
        # popleft at the front, which is exactly what a FIFO queue needs.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # New values join at the BACK of the line, so earlier arrivals (already
        # at the front) are still served first -> this is what makes it FIFO.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Dequeuing an empty queue is an invalid operation, so we return None
        # (and print a warning) instead of crashing the program.
        if self.is_empty():
            print("  [Queue.dequeue] ERROR: cannot dequeue an empty queue (returning None).")
            return None
        # popleft() removes and returns the front (earliest arrival) item.
        return self._items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # front() is a "look, don't touch" read: it shows who is next in line
        # (the oldest value) without removing them from the queue.
        if self.is_empty():
            print("  [Queue.front] ERROR: cannot view the front of an empty queue (returning None).")
            return None
        return self._items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # True when the deque holds no items (length 0).
        return len(self._items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Real-world scenario: a text editor's "Undo" history. Every action is
    # pushed onto the stack, and Undo pops the most recent action first.
    # Requirements: create a stack, add 4+ values, show LIFO, and handle the
    # edge cases (pop/peek on empty, single-item stack).

    print("\n=== STACK DEMO: Text Editor Undo History ===")

    # 1. Create a Stack object (a fresh, empty undo history).
    undo_stack = Stack()

    # 2. Add 4 editing actions to the stack (each becomes "the newest").
    undo_stack.push("typed 'hello'")
    undo_stack.push("applied bold")
    undo_stack.push("inserted image")
    undo_stack.push("deleted a paragraph")

    # 3. peek() shows the top (most recent) action without removing it.
    print(f"After 4 actions, top of stack (most recent): '{undo_stack.peek()}'")

    # 4. Demonstrate LIFO: Undo removes the most recently added action first.
    print("\nUndoing actions (LIFO - most recent first):")
    while not undo_stack.is_empty():
        print(f"  Undo '{undo_stack.pop()}'")

    # 5. Edge case: pop() on an empty stack is handled safely (returns None).
    print("\nTrying to undo with an empty history:")
    undo_stack.pop()

    # 6. Edge case: peek() on an empty stack is handled safely (returns None).
    print("Trying to peek at an empty history:")
    undo_stack.peek()

    # 7. Edge case: single-item stack -> push one, pop it, verify it is empty.
    undo_stack.push("typed 'final word'")
    print(f"\nSingle-item stack -> pop returned '{undo_stack.pop()}'.")
    print(f"Stack empty after removal? {undo_stack.is_empty()}")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Real-world scenario: a coffee shop customer line. Customers join at the
    # back and are served in the order they arrived (first come, first served).
    # Requirements: create a queue, add 4+ values, show FIFO, and handle the
    # edge cases (dequeue/front on empty, single-item queue).

    print("\n=== QUEUE DEMO: Coffee Shop Customer Line ===")

    # 1. Create a Queue object (an empty customer line).
    coffee_line = Queue()

    # 2. Add 4 customers to the back of the line.
    coffee_line.enqueue("Alex")
    coffee_line.enqueue("Jordan")
    coffee_line.enqueue("Sam")
    coffee_line.enqueue("Riley")

    # 3. front() shows who is next in line without removing them.
    print(f"After 4 customers arrive, next in line: '{coffee_line.front()}'")

    # 4. Demonstrate FIFO: serve customers in arrival order.
    print("\nServing customers (FIFO - first come, first served):")
    while not coffee_line.is_empty():
        print(f"  Serving '{coffee_line.dequeue()}'")

    # 5. Edge case: dequeue() on an empty queue is handled safely (returns None).
    print("\nTrying to serve with an empty line:")
    coffee_line.dequeue()

    # 6. Edge case: front() on an empty queue is handled safely (returns None).
    print("Trying to view the front of an empty line:")
    coffee_line.front()

    # 7. Edge case: single-item queue -> enqueue one, dequeue it, verify empty.
    coffee_line.enqueue("Taylor")
    print(f"\nSingle-item queue -> dequeue returned '{coffee_line.dequeue()}'.")
    print(f"Queue empty after removal? {coffee_line.is_empty()}")


if __name__ == "__main__":
    main()
