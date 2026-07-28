import cv2

cap = cv2.VideoCapture("input.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Fast Motion", frame)

    # Fast motion (decrease delay)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()