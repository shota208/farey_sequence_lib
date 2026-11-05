# farey_sequence_lib

Generate the Farey sequence of order `n`: every reduced fraction between 0 and 1 whose denominator is at most `n`, in ascending order.

```python
from farey_sequence_lib import farey_length, farey_sequence

farey_sequence(4)
# [(0, 1), (1, 4), (1, 3), (1, 2), (2, 3), (3, 4), (1, 1)]

farey_length(4)
# 7
```

Both functions are exported from the package root. `farey_sequence(n)` returns a list of `(numerator, denominator)` integer pairs in lowest terms. `farey_length(n)` returns the number of terms without building the list.

## Why this exists

The Farey sequence is small to state but fiddly to produce correctly: naive generation builds every fraction `a/b` with `b <= n`, reduces it, and sorts, which is both slower than necessary and easy to get subtly wrong around the endpoints and duplicates. This library uses the standard neighbour recurrence, so each term is emitted already reduced and already ordered. The trade-off is that the recurrence is less obvious to read than a reduce-and-sort loop; the code documents the step so the correctness argument is visible.

`farey_length` computes `1 + sum(phi(k), k=1..n)` with a totient sieve instead of calling `farey_sequence(n)` and taking `len`. That is the whole reason it exists as a separate function.

## Edge cases

Orders below 1 have no fractions in `[0, 1]`, so `farey_sequence(0)` and `farey_sequence(-3)` return `[]`, and `farey_length` returns `0` for those inputs. Order 1 is the smallest non-empty sequence and is `[(0, 1), (1, 1)]`.

## Tests

```
PYTHONPATH=src python -m unittest discover -s tests
```
