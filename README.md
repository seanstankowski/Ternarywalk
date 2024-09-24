# Ternarywalk

This tool calculates the 1D distance between consecutive rows in a dataset that represent points in a ternary space. A ternary plot is used to visualize data composed of three components that sum to a constant value. The distance between two points in this space is computed using Euclidean distance, but modified for the triangular coordinate system used in ternary plots.

## Mathematical Background

Each row in the input dataset has three values, `t1`, `t2`, and `t3`, which represent counts that sum to a constant (in this case, 10,000). The points are transformed into a 2D Euclidean space using the barycentric coordinates for the ternary plot, and then the Euclidean distance between consecutive rows is calculated.
```math
t1 + t2 + t3 = 1

