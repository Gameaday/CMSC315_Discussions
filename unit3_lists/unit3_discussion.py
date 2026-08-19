"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Python's list.insert mutates the list in place, placing `value` at `index`.
    # Every element currently at `index` or later is shifted one position to the
    # right to make room. Performance depends on location:
    #   - Beginning (index 0): every existing element shifts -> O(n).
    #   - Middle: only the tail after the index shifts -> up to O(n).
    #   - End: nothing shifts (appends effectively) -> amortized O(1).
    # Python also clamps out-of-range indexes (too small -> front, too large ->
    # back) instead of raising, so this stays safe even on invalid input.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Validation first: a negative index, or one >= len(lst), does not exist.
    # Without this check, lst.pop(index) would raise IndexError and crash the
    # program. Returning None turns an invalid operation into a safe, testable
    # edge case instead of a runtime failure.
    if index < 0 or index >= len(lst):
        return None
    # pop(index) removes and returns that element; everything after it shifts
    # left by one to close the gap (O(n) worst case from the front).
    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search: it scans the list one element at a time, in
    # order, because a plain Python list gives no shortcut to find a value
    # (only index-based random access). It stops at the first match, so in the
    # worst case it examines every element -> O(n).
    for i, item in enumerate(lst):
        if item == value:
            return i
    # Return -1 (not None) so callers can distinguish "not found" from an
    # element that literally equals None.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")
    print("Scenario: managing a music streaming 'playlist' as an array-based list.")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # 1. Start with a small "playlist" of song titles (our array-based list).
    playlist = ["Taylor Swift - Cruel Summer", "The Weeknd - Blinding Lights",
                "Bad Bunny - MONACO", "SZA - Kill Bill"]
    print(f"Original playlist ({len(playlist)} songs): {playlist}")

    # 2. Insert at the END (amortized O(1) - no elements shift).
    #    A listener adds the next track to the bottom of the queue.
    insert_at(playlist, len(playlist), "Dua Lipa - Houdini")
    print(f"After inserting at end:   {playlist}")

    # 3. Insert at the BEGINNING (O(n) - every song shifts right one slot).
    #    "Recently added" pins the brand-new release to the top of the list.
    insert_at(playlist, 0, "Beyonce - TEXAS HOLD 'EM")
    print(f"After inserting at start: {playlist}")

    # 4. Insert in the MIDDLE (shifts only the tail after the index).
    #    The user inserts a track directly after the currently-playing song.
    insert_at(playlist, 2, "Drake - Rich Baby Daddy")
    print(f"After inserting at index 2: {playlist}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Delete from the BEGINNING (O(n) shift). Removing the current song skips
    # to the next one; every remaining song moves one slot left.
    removed = delete_at(playlist, 0)
    print(f"Removed from start:  '{removed}'")
    print(f"Updated playlist:    {playlist}")

    # Delete from the MIDDLE (shifts the tail left).
    removed = delete_at(playlist, 2)
    print(f"Removed from middle: '{removed}'")
    print(f"Updated playlist:    {playlist}")

    # Delete from the END (O(1) - no shifting, just truncates).
    removed = delete_at(playlist, len(playlist) - 1)
    print(f"Removed from end:    '{removed}'")
    print(f"Updated playlist:    {playlist}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Search for a song that EXISTS: linear scan returns its index.
    found = search_value(playlist, "SZA - Kill Bill")
    print(f"Searching for 'SZA - Kill Bill': found at index {found}")

    # Search for a song that does NOT exist: linear scan returns -1.
    found = search_value(playlist, "Tupac - Changes")
    print(f"Searching for 'Tupac - Changes':  not found -> index {found}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge 1: delete with an INVALID index (out of range). delete_at validates
    # and returns None instead of raising IndexError, so the program continues.
    result = delete_at(playlist, 99)
    print(f"delete_at(playlist, 99) -> {result} (invalid index, list unchanged: {playlist})")

    # Edge 2: delete from an EMPTY list. len is 0, so index 0 is invalid -> None.
    empty_playlist = []
    print(f"\nDeleting from an empty list -> {delete_at(empty_playlist, 0)} (no crash)")

    # Edge 3: insert into an EMPTY list. insert() accepts index 0 on an empty
    # list, placing the first song cleanly.
    insert_at(empty_playlist, 0, "Coldplay - Viva La Vida")
    print(f"Inserting into an empty list -> {empty_playlist}")

    # Edge 4: search an EMPTY list (linear scan finds nothing -> -1).
    print(f"Searching an empty list -> {search_value(empty_playlist, 'anything')} (not found)")


if __name__ == "__main__":
    main()