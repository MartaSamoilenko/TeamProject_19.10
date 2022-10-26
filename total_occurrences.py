def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 2
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    0
    """
    count = 0
    if ch in s1:
        for element in s1:
            if element == ch:
                count += 1
    if ch in s2:
        for element in s2:
            if element == ch:
                count += 1

    return count

if __name__ == "__main__":
   import doctest
   print(doctest.testmod())