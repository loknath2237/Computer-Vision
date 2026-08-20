import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Get image dimensions
height, width = image.shape[:2]

# Define four points in the original image
points1 = np.float32([
    [50, 50],
    [width - 50, 50],
    [50, height - 50],
    [width - 50, height - 50]
])

# Define four points for perspective transformation
points2 = np.float32([
    [100, 100],
    [width - 100, 50],
    [50, height - 100],
    [width - 50, height - 50]
])

# Calculate Perspective Transformation Matrix
matrix = cv2.getPerspectiveTransform(points1, points2)

# Apply Perspective Transformation
perspective = cv2.warpPerspective(image, matrix, (width, height))

# Save the output image
cv2.imwrite("perspective_transformed.jpg", perspective)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective)

cv2.waitKey(0)
cv2.destroyAllWindows()