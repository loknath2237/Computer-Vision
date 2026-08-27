import cv2
import os

# Load OpenCV DNN face detector
model = cv2.FaceDetectorYN.create(
    "face_detection_yunet_2023mar.onnx",
    "",
    (320, 320),
    0.6,
    0.3,
    5000
)

# Read input image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# Get image size
height, width = image.shape[:2]

# Set input size
model.setInputSize((width, height))

# Detect faces
_, faces = model.detect(image)

count = 0

if faces is not None:
    for face in faces:

        count += 1

        x, y, w, h = face[:4].astype(int)

        # Draw rectangle
        cv2.rectangle(
            image,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )

        # Confidence score
        confidence = face[-1]

        cv2.putText(
            image,
            f"Face {count}: {confidence:.2f}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

print("Number of faces detected:", count)

# Save output
output_path = os.path.join(os.getcwd(), "output.jpg")
cv2.imwrite(output_path, image)

print("Output saved to:", output_path)

# Display result
cv2.imshow("Accurate Face Detection", image)

cv2.waitKey(0)
cv2.destroyAllWindows()