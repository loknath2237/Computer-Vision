
import cv2
import sys
import os


def rotate_180_y(image):
	# 180-degree rotation around y-axis for a 2D image is a horizontal flip
	return cv2.flip(image, 1)


def main():
	if len(sys.argv) < 2:
		print("Usage: python 180.py <input_image> [output_image]")
		return

	inp = sys.argv[1]
	out = sys.argv[2] if len(sys.argv) > 2 else 'rotated_180_y.jpg'

	img = cv2.imread(inp)
	if img is None:
		print(f"Failed to load image: {inp}")
		return

	# Display input image
	cv2.imshow('Input Image', img)
	print(f"Loaded input image: {inp}")
	print(f"Image shape: {img.shape}")

	# Rotate 180 degrees around y-axis
	res = rotate_180_y(img)
	
	# Display output image
	cv2.imshow('Output Image - 180° Rotation (Y-axis)', res)
	
	# Save output image
	cv2.imwrite(out, res)
	print(f"Saved: {out}")
	
	# Wait for key press to close windows
	print("Press any key to close the windows...")
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()

