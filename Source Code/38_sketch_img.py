# Import required libraries
import cv2

# Load the image
filename = 'iron.jpg'
img = cv2.imread(filename)

# Convert image into gray_scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_gray_img = cv2.bitwise_not(gray_img) 

# convert inverted image into a blur image
blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

# Inverting the image the blurred image
inverted_blurred_img = cv2.bitwise_not(blurred_img)

#Final Output as Pencil Sketch
pencil_sketch_IMG = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

# Save the image
cv2.imwrite('sketch.png', pencil_sketch_IMG)
