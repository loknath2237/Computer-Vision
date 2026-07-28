import cv2

cap = cv2.VideoCapture("input.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Slow Motion", frame)

    # Slow motion (increase delay)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()