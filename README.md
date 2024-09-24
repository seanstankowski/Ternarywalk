# Ternary Distance Calculator

This repository provides a Python script to calculate the Euclidean distance between consecutive points in a ternary plot. The ternary plot represents three variables (`t1`, `t2`, `t3`) which sum to a constant number (in this case, 10,000). The script converts these ternary coordinates to Cartesian coordinates and computes the distance between consecutive rows in the input data, outputting a vector of distances.

## Mathematical Overview

### Ternary Coordinates

A ternary plot is a triangular plot used to visualize the proportions of three variables that sum to a constant. In this case, the variables `t1`, `t2`, and `t3` sum to 10,000. For easier distance calculations, these values are first normalized so that:

$$t1 + t2 + t3 = 1$$

### Conversion from Ternary to Cartesian Coordinates

To calculate distances, we need to convert the ternary coordinates to Cartesian (2D) coordinates.

Given normalized ternary coordinates `(t1, t2, t3)`, the Cartesian coordinates `(x, y)` are calculated as:

$$x = 0.5 * (2 * t2 + t1) y = (sqrt(3) / 2) * t1$$


These formulas are derived from the geometry of the equilateral triangle representing the ternary plot.

### Distance Calculation

Once the ternary coordinates are converted to Cartesian coordinates, the Euclidean distance between two consecutive points `(x1, y1)` and `(x2, y2)` is calculated as:

$$d = sqrt((x2 - x1)^2 + (y2 - y1)^2)$$

This formula calculates the straight-line distance between the two points.

## Installation

To run the script, ensure you have Python installed along with the necessary libraries:

```bash
pip install pandas numpy
```
## Usage
To calculate the distances between consecutive rows of a CSV file, run the script from the terminal with the following command:

```bash
python ternary_distance.py <input_file.csv> <output_file.csv>
```

The input CSV file must contain at least three columns labeled t1, t2, and t3. Each row represents the counts for three components that sum to a constant. The output file will be a CSV with one column named distance. This column will contain the Euclidean distances between consecutive points in the ternary plot.
