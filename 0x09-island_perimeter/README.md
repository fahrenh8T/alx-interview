# 0x09. Island Perimeter

Create a function named `island_perimeter(grid)` that calculates the perimeter of an island within a given grid. The grid is represented as a list of lists containing integers, where:

- The number `0` represents water.
- The number `1` represents land.

Specifications for the grid:

- Each cell in the grid is square with each side measuring 1 unit.
- Cells connect either horizontally or vertically (not diagonally).
- The grid is rectangular and its dimensions (width and height) do not exceed 100 units.

Additional details about the grid:

- The grid is entirely surrounded by water.
- There is only one island in the grid, and it does not contain any "lakes" (areas of water enclosed by land and not connected to the outer water).

The function should return the perimeter of the island, measured in the same unit as the sides of the grid cells.
