import cv2

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Enlarge the image (2x)
bigger = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Shrink the image (0.5x)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Save the resized images
cv2.imwrite("bigger_image.jpg", bigger)
cv2.imwrite("smaller_image.jpg", smaller)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()