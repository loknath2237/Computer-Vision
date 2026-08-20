import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Dilation
dilated = cv2.dilate(image, kernel, iterations=1)

# Save the output image
cv2.imwrite("dilation_output.jpg", dilated)

# Display original and dilated images
cv2.imshow("Original Image", image)
cv2.imshow("Dilation Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()