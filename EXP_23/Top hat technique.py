import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Top Hat operation
# Top Hat = Original Image - Opening
top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

# Save the output image
cv2.imwrite("top_hat_output.jpg", top_hat)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Top Hat Image", top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()