import cv2

# Read the original image
image = cv2.imread("input.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Create watermark text
watermark = image.copy()

# Watermark settings
text = "WATERMARK"
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 2
thickness = 3

# Get image dimensions
height, width = image.shape[:2]

# Position of watermark
text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
x = width - text_size[0] - 30
y = height - 30

# Add watermark text
cv2.putText(
    watermark,
    text,
    (x, y),
    font,
    font_scale,
    (255, 255, 255),
    thickness,
    cv2.LINE_AA
)

# Blend original image and watermark
result = cv2.addWeighted(image, 0.8, watermark, 0.2, 0)

# Save the watermarked image
cv2.imwrite("watermarked_image.jpg", result)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Watermarked Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()