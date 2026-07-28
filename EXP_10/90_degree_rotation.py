import cv2

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Rotate the image 90 degrees clockwise
rotated = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Save the output image
cv2.imwrite("rotated_image.jpg", rotated)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()