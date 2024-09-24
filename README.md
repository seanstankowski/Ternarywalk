# Ternary Distance Calculator

This repository provides a Python script to calculate the Euclidean distance between consecutive points in a ternary plot. The ternary plot represents three variables (`t1`, `t2`, `t3`) which sum to a constant number (in this case, 10,000). The script converts these ternary coordinates to Cartesian coordinates and computes the distance between consecutive rows in the input data, outputting a vector of distances.

## Mathematical Overview

### Ternary Coordinates

A ternary plot is a triangular plot used to visualize the proportions of three variables that sum to a constant. In this case, the variables `t1`, `t2`, and `t3` sum to 10,000. For easier distance calculations, these values are first normalized so that:


$$t1 + t2 + t3 = 1$$
