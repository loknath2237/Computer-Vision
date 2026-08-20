import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convert grayscale image to float32
gray = np.float32(gray)

# Apply Harris Corner Detection
corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

# Dilate the corners to make them visible
corners = cv2.dilate(corners, None)

# Mark detected corners in red
image[corners > 0.01 * corners.max()] = [0, 0, 255]

# Save the output image
cv2.imwrite("harris_corners.jpg", image)

# Display the result
cv2.imshow("Harris Corner Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()