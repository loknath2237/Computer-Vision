import cv2

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Sobel filter in X direction
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Apply Sobel filter in Y direction
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to absolute values
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y gradients
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

# Save the output images

cv2.imwrite("sobel_output.jpg", sobel)

# Display the images
cv2.imshow("Original Image", image)

cv2.imshow("Sobel Filtered Image", sobel)

cv2.waitKey(0)
cv2.destroyAllWindows()