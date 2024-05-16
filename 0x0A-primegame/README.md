# Prime Game

## Overview

The Prime Game is a game where two players, Maria and Ben, take turns selecting prime numbers from a given range. The winner is determined based on the number of prime numbers selected during each round.

This document provides an overview of the functions used in the Prime Game implementation.

## Functions

### `primeNumbers(n)`

Returns a list of prime numbers between 1 and `n` inclusive.

#### Arguments

- `n` (int): The upper boundary of the range (inclusive). The lower boundary is always 1.

#### Returns

- `List[int]`: A list of prime numbers between 1 and `n` inclusive.

#### Example

```python
>>> primeNumbers(10)
[2, 3, 5, 7]
