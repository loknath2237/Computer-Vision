import cv2

# Read the image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray, 100, 200)

# Save the output image
cv2.imwrite("output_canny.jpg", edges)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
