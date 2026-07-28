import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Create a 5x5 kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Erosion
eroded = cv2.erode(image, kernel, iterations=1)

# Save the output image
cv2.imwrite("eroded_image.jpg", eroded)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()