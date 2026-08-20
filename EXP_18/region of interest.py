import cv2

# Read the source image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Select the Region of Interest (ROI)
x = 100
y = 100
width = 300
height = 200

# Crop the ROI
roi = image[y:y + height, x:x + width]

# Copy the ROI
roi_copy = roi.copy()

# Paste the copied ROI to a new location
paste_x = 400
paste_y = 100

image[paste_y:paste_y + height, paste_x:paste_x + width] = roi_copy

# Save the cropped ROI
cv2.imwrite("cropped_roi.jpg", roi)


cv2.imshow("Cropped ROI", roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
