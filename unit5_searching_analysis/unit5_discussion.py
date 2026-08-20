"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Linear search checks each element one at a time, in order, using
    # enumerate() so we get both the index and the value. This works on any
    # list, sorted or not. In the worst case - target at the very end or not
    # present at all - it examines every element, so the cost grows directly
    # with the size of the list -> O(n) time complexity.
    for i, item in enumerate(lst):
        if item == target:
            return i
    # Not found anywhere in the list.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Binary search only works because the list is sorted. We track the bounding
    # indexes low..high and inspect the middle each step. Each comparison either
    # finds the target or tells us which half it must be in, so we throw away the
    # other half. This halves the search space every iteration, giving O(log n)
    # time instead of linear search's O(n).
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        if target < lst[mid]:
            high = mid - 1  # target must be in the left half
        else:
            low = mid + 1   # target must be in the right half
    # The bound ran past itself without finding the target.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # A small, SORTED catalog of song IDs on a streaming service. Both algorithms
    # work here because the data is sorted (which binary search requires).
    small_songs = [101, 205, 342, 488, 512, 699, 743]
    print(f"Sorted song IDs: {small_songs}")

    # Search for a value that EXISTS (488). Both return its index.
    print(f"\nLooking for song 488:")
    print(f"  linear_search -> index {linear_search(small_songs, 488)}")
    print(f"  binary_search -> index {binary_search(small_songs, 488)}")

    # Search for a value that does NOT exist. Both return -1.
    print(f"\nLooking for song 900 (not present):")
    print(f"  linear_search -> index {linear_search(small_songs, 900)}")
    print(f"  binary_search -> index {binary_search(small_songs, 900)}")

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # A much larger sorted dataset (10,000 consecutive IDs) to stress both
    # algorithms. Linear search may scan many elements; binary search only
    # needs ~log2(10000) ~ 14 comparisons.
    big_songs = list(range(10000))

    # Small helpers that count how many comparisons each algorithm makes, so we
    # can see binary search pull ahead as n grows.
    def linear_count(lst, target):
        steps = 0
        for i, item in enumerate(lst):
            steps += 1
            if item == target:
                return i, steps
        return -1, steps

    def binary_count(lst, target):
        steps = 0
        low, high = 0, len(lst) - 1
        while low <= high:
            steps += 1
            mid = (low + high) // 2
            if lst[mid] == target:
                return mid, steps
            if target < lst[mid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1, steps

    # A value that exists near the END of the big list. Linear search scans
    # almost every element; binary search halves its way there in ~14 steps.
    li, ls = linear_count(big_songs, 9999)
    bi, bs = binary_count(big_songs, 9999)
    print(f"Found song 9999 -> linear: index {li} in {ls} comparisons; "
          f"binary: index {bi} in {bs} comparisons.")

    # A value NOT present. Linear search must check all 10,000; binary search
    # concludes in ~log2(10000) comparisons.
    li, ls = linear_count(big_songs, 15000)
    bi, bs = binary_count(big_songs, 15000)
    print(f"Song 15000 (missing) -> linear: index {li} in {ls} comparisons; "
          f"binary: index {bi} in {bs} comparisons.")

    # Because linear search checks every element (O(n)) while binary search cuts
    # the remaining range in half each step (O(log n)), the gap widens as n grows:
    # 10,000 elements → ~10,000 vs ~14 comparisons here.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge 1: EMPTY list. Both loops run zero times and return -1.
    empty = []
    print(f"Empty list -> linear: {linear_search(empty, 5)}, "
          f"binary: {binary_search(empty, 5)}")

    # Edge 2: SINGLE-element list, target present and absent.
    only = [42]
    print(f"Single element [42] -> linear found: {linear_search(only, 42)}, "
          f"binary found: {binary_search(only, 42)}; "
          f"binary missing: {binary_search(only, 7)}")

    # Edge 3: target at the FIRST position (best case for linear, index 0).
    data = [5, 10, 15]
    print(f"Target at first position -> linear: {linear_search(data, 5)}, "
          f"binary: {binary_search(data, 5)}")

    # Edge 4: target at the LAST position (worst case for linear).
    print(f"Target at last position -> linear: {linear_search(data, 15)}, "
          f"binary: {binary_search(data, 15)}")


if __name__ == "__main__":
    main()