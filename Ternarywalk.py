import pandas as pd
import numpy as np
import sys

def normalize_counts(row, total):
    """
    Normalize the counts in a row so they sum to 1.
    """
    return row / total

def ternary_to_cartesian(t1, t2, t3):
    """
    Convert ternary coordinates to 2D Cartesian coordinates.
    """
    x = 0.5 * (2 * t2 + t1)
    y = (np.sqrt(3) / 2) * t1
    return x, y

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate Euclidean distance between two points in Cartesian space.
    """
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main(input_file, output_file):
    # Read the CSV file
    data = pd.read_csv(input_file)

    # Assuming the total is 10000 (if the total can vary, you can adjust how you get the total value)
    total = 10000

    # Normalize the counts so that t1 + t2 + t3 = 1 for each row
    data[['t1', 't2', 't3']] = data[['t1', 't2', 't3']].apply(normalize_counts, total=total, axis=1)

    # Calculate distances between consecutive rows
    distances = []
    for i in range(1, len(data)):
        # Get ternary values for the current and previous rows
        t1_prev, t2_prev, t3_prev = data.iloc[i - 1][['t1', 't2', 't3']]
        t1_curr, t2_curr, t3_curr = data.iloc[i][['t1', 't2', 't3']]

        # Convert ternary coordinates to Cartesian
        x_prev, y_prev = ternary_to_cartesian(t1_prev, t2_prev, t3_prev)
        x_curr, y_curr = ternary_to_cartesian(t1_curr, t2_curr, t3_curr)

        # Calculate Euclidean distance between the current row and the previous row
        dist = calculate_distance(x_prev, y_prev, x_curr, y_curr)
        distances.append(dist)

    # Add a NaN or 0 for the first row (which has no previous row to compare)
    distances = [np.nan] + distances

    # Save distances to the output file
    output_df = pd.DataFrame({'distance': distances})
    output_df.to_csv(output_file, index=False)
    print(f"Distances saved to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_file.csv> <output_file.csv>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)