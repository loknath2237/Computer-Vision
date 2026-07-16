import cv2

# Read the image
image = cv2.imread("input.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Apply Gaussian Blur
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# Save the blurred image
cv2.imwrite("blur_output.jpg", blurred)

# Display the images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()