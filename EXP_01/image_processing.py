import cv2

# Read the image
image = cv2.imread("input.jpg")

# Check if image loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite("gray_output.jpg", gray)

    # Display images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()