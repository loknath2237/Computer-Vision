import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Closing operation
# Closing = Dilation followed by Erosion
closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

# Save the output image
cv2.imwrite("closing_output.jpg", closing)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Closing Image", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()