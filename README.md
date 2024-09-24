# Ternarywalk

This tool calculates the 1D distance between consecutive rows in a dataset that represent points in a ternary space. A ternary plot is used to visualize data composed of three components that sum to a constant value. The distance between two points in this space is computed using Euclidean distance, but modified for the triangular coordinate system used in ternary plots.

## Mathematical Background

Each row in the input dataset has three values, `t1`, `t2`, and `t3`, which represent counts that sum to a constant (in this case, 10,000). The points are transformed into a 2D Euclidean space using the barycentric coordinates for the ternary plot, and then the Euclidean distance between consecutive rows is calculated.

### Barycentric Coordinates Transformation

Given three values `t1`, `t2`, and `t3`, the transformation into 2D coordinates is done as follows:

1. Convert `t1`, `t2`, and `t3` into proportions by dividing by their sum.
   \[
   t1' = \frac{t1}{t1 + t2 + t3}
   \]
   \[
   t2' = \frac{t2}{t1 + t2 + t3}
   \]
   \[
   t3' = \frac{t3}{t1 + t2 + t3}
   \]

2. Transform these into 2D coordinates using barycentric coordinates. The formulas for transforming the proportions into 2D Cartesian coordinates are:

   \[
   x = \frac{1}{2} \times (2 \times t2' + t3')
   \]
   \[
   y = \frac{\sqrt{3}}{2} \times t3'
   \]

   Here, `x` and `y` are the coordinates for each point on the ternary plot in a 2D Euclidean plane.

### Euclidean Distance Calculation

Once the points are transformed into 2D coordinates, the distance between consecutive points (rows) is calculated using the Euclidean distance formula:

\[
d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}
\]

Where:

- \( (x_1, y_1) \) and \( (x_2, y_2) \) are the 2D coordinates of consecutive points.

This calculation is done for each pair of consecutive rows in the dataset to produce a vector of distances.
