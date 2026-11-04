"""Core implementation of Farey sequence generation.

The Farey sequence of order n is the sorted list of reduced fractions in [0, 1]
whose denominators are at most n. The sequence always begins with 0/1 and ends
with 1/1.

We generate the sequence directly with the standard recurrence rather than
building all fractions and reducing them. The recurrence is O(len(sequence))
in time and O(1) extra space per step, which matters because the sequence grows
as roughly 3 n^2 / pi^2. Generating by reduction would be O(n^2 log n) and would
allocate a large intermediate list.
"""

from __future__ import annotations

from typing import Iterator, List, Tuple


def farey_sequence(n: int) -> List[Tuple[int, int]]:
    """Return the Farey sequence of order *n* as a list of ``(numerator, denominator)``.

    The fractions are in ascending order and each is in lowest terms. The
    sequence is empty for ``n < 1`` because no fraction with denominator at
    least 1 fits in [0, 1] when the order is below 1.

    Example:
        >>> farey_sequence(4)
        [(0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1)]
    """
    if n < 1:
        return []
    return list(_farey_iter(n))


def farey_length(n: int) -> int:
    """Return the number of fractions in the Farey sequence of order *n*.

    This is 1 + sum(phi(k) for k in 1..n) when *n* >= 1, and 0 otherwise.
    Computing it directly with a totient sieve is faster than materialising the
    whole sequence when only the count is needed.
    """
    if n < 1:
        return 0
    phi = _totients_up_to(n)
    return 1 + sum(phi[1:])


def _farey_iter(n: int) -> Iterator[Tuple[int, int]]:
    """Yield the Farey sequence of order *n* in order.

    This is the classic next-term recurrence: given consecutive terms a/b and
    c/d, the next denominator is ``k = (n + b) // d`` and the next term is
    ``(k*c - a, k*d - b)``. The recurrence keeps every term reduced by
    construction, so no gcd is needed.
    """
    a, b = 0, 1
    c, d = 1, n
    yield (a, b)
    while c <= n:
        yield (c, d)
        k = (n + b) // d
        a, b, c, d = c, d, k * c - a, k * d - b


def _totients_up_to(n: int) -> List[int]:
    """Return ``[0, phi(1), phi(2), ..., phi(n)]`` using a linear sieve."""
    phi = list(range(n + 1))
    for i in range(2, n + 1):
        if phi[i] == i:  # i is prime
            for j in range(i, n + 1, i):
                phi[j] -= phi[j] // i
    return phi
