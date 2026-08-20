import cv2

# Read the input video
cap = cv2.VideoCapture("input.mp4")

if not cap.isOpened():
    print("Error: Video not found!")
    exit()

# Store all frames
frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

# Get video properties
width = int(frames[0].shape[1])
height = int(frames[0].shape[0])
fps = 30

# Create output video
out = cv2.VideoWriter(
    "reverse_video.mp4",
    cv2.VideoWriter_fourcc(*"mp4v"),
    fps,
    (width, height)
)

# Write frames in reverse order
for frame in reversed(frames):
    out.write(frame)

    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()