import cv2
from ultralytics import YOLO
import os

# Load YOLO model
model = YOLO("yolo11n.pt")

# Input image
input_image = "input.jpg"

# Read image
image = cv2.imread(input_image)

if image is None:
    print("Error: input.jpg not found")
    exit()

# Detect objects
results = model(image)

watch_found = False

for result in results:

    for box in result.boxes:

        confidence = float(box.conf[0])

        if confidence >= 0.25:

            class_id = int(box.cls[0])
            object_name = model.names[class_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box
            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                3
            )

            # Display label
            label = f"{object_name} {confidence:.2f}"

            cv2.putText(
                image,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

            print("Detected:", object_name)

            if object_name.lower() in ["watch", "clock"]:
                watch_found = True

# Save output in the same folder
folder = os.path.dirname(os.path.abspath(input_image))
output_path = os.path.join(folder, "output.jpg")

cv2.imwrite(output_path, image)

if watch_found:
    print("\nWATCH DETECTED")
else:
    print("\nWATCH NOT DETECTED")

print("Output saved to:")
print(output_path)

# Show result
cv2.imshow("Object Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()