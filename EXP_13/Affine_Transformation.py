import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
rows, cols = image.shape[:2]

# Define three points from the original image
points1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Define corresponding points for transformation
points2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Calculate the Affine Transformation Matrix
matrix = cv2.getAffineTransform(points1, points2)

# Apply Affine Transformation
affine = cv2.warpAffine(image, matrix, (cols, rows))

# Save the output image
cv2.imwrite("affine_transformed.jpg", affine)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformed Image", affine)

cv2.waitKey(0)
cv2.destroyAllWindows()