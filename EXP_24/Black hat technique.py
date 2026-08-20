import cv2
import numpy as np

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Create a kernel
kernel = np.ones((5, 5), np.uint8)

# Apply Black Hat operation
# Black Hat = Closing - Original Image
black_hat = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

# Save the output image
cv2.imwrite("black_hat_output.jpg", black_hat)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Black Hat Image", black_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()