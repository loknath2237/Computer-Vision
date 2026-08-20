import cv2

# Read input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Threshold the image
_, thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)

# Find contours
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Detect object
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)

    if w > 30 and h > 30:
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        cv2.putText(
            image,
            "Watch",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

# Save output
cv2.imwrite("watch_detection.jpg", image)

# Display result
cv2.imshow("Watch Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()