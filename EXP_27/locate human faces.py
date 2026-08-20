import cv2

# Read the input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect face-like regions using thresholding
gray = cv2.equalizeHist(gray)

_, binary = cv2.threshold(
    gray,
    100,
    255,
    cv2.THRESH_BINARY
)

# Find contours
contours, _ = cv2.findContours(
    binary,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Locate human face regions
for contour in contours:

    x, y, w, h = cv2.boundingRect(contour)

    # Face-like size and shape
    if w > 50 and h > 50 and 0.6 < w / h < 1.5:

        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

# Save result
cv2.imwrite("face_detection.jpg", image)

# Display result
cv2.imshow("Human Face Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()