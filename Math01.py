import math

# This script computes the distance between two points in 3D space.
# You can easily extend this to multiple points if you wish!

def get_point(index):
    """Prompts the user for a 3D point and returns it as a tuple (x, y, z)."""
    print(f"\nEnter coordinates for point {index}:")
    x = float(input("  x: "))
    y = float(input("  y: "))
    z = float(input("  z: "))
    return (x, y, z)

# Collect two points from the user
point1 = get_point(1)
point2 = get_point(2)

# Calculate the Euclidean distance between them
distance = math.sqrt(
    (point1[0] - point2[0]) ** 2 +
    (point1[1] - point2[1]) ** 2 +
    (point1[2] - point2[2]) ** 2
)

print(f"\nThe distance between the points {point1} and {point2} is: {distance:.4f}")
