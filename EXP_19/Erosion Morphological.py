import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Save the output image
cv2.imwrite("erosion_output.jpg", eroded)

# Display original and eroded images
cv2.imshow("Original Image", image)
cv2.imshow("Erosion Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()