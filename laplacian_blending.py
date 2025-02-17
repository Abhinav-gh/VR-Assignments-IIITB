import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def build_gaussian_pyramid(image, levels):
    """Builds a Gaussian Pyramid for an image."""
    pyramid = [image]
    for i in range(levels-1):
        image = cv.pyrDown(image)
        pyramid.append(image)
    return pyramid

def build_laplacian_pyramid(image, levels):
    """Builds a Laplacian Pyramid for an image."""
    gaussian_pyramid = build_gaussian_pyramid(image, levels)
    laplacian_pyramid = []
    
    for i in range(levels-1):
        size = (gaussian_pyramid[i].shape[1], gaussian_pyramid[i].shape[0])
        upsampled = cv.pyrUp(gaussian_pyramid[i+1], dstsize=size)
        laplacian = cv.subtract(gaussian_pyramid[i], upsampled)
        laplacian_pyramid.append(laplacian)
    
    laplacian_pyramid.append(gaussian_pyramid[-1])  # Last level is the same as Gaussian
    return laplacian_pyramid

def laplacian_blend(img1, img2, mask, levels=6):
    """Blends two images using Laplacian Pyramid Blending."""
    
    # Build Laplacian Pyramids for both images
    laplacian_pyramid1 = build_laplacian_pyramid(img1, levels)
    laplacian_pyramid2 = build_laplacian_pyramid(img2, levels)
    
    # Build Gaussian Pyramid for the mask
    gaussian_pyramid_mask = build_gaussian_pyramid(mask, levels)
    
    # Blend the Laplacian Pyramids at each level
    blended_pyramid = []
    for i in range(levels):
        blended = cv.multiply(gaussian_pyramid_mask[i], laplacian_pyramid1[i]) + \
                 cv.multiply(1 - gaussian_pyramid_mask[i], laplacian_pyramid2[i])
        blended_pyramid.append(blended)
    
    # Reconstruct the final image
    blended_image = blended_pyramid[-1]
    for i in range(levels-2, -1, -1):
        size = (blended_pyramid[i].shape[1], blended_pyramid[i].shape[0])
        blended_image = cv.pyrUp(blended_image, dstsize=size)
        blended_image = cv.add(blended_pyramid[i], blended_image)
    
    return blended_image

# Load images and mask
img1 = cv.imread('panorama1.jpg')  # Replace with your image path
img2 = cv.imread('panorama2.jpg')  # Replace with your image path

# Ensure both images are of the same size
img1 = cv.resize(img1, (img2.shape[1], img2.shape[0]))

# Create a mask (you can replace this with your own mask)
mask = np.zeros_like(img1, dtype=np.float32)
mask[:, :img1.shape[1]//2] = 1  # This creates a left-right mask

# Perform Laplacian Pyramid Blending
blended_image = laplacian_blend(img1, img2, mask)

# Convert to RGB for display
blended_image_rgb = cv.cvtColor(blended_image, cv.COLOR_BGR2RGB)

# Display the result
plt.figure(figsize=(10, 10))
plt.imshow(blended_image_rgb)
plt.axis('off')
plt.title('Laplacian Pyramid Blended Image')
plt.show()

# Save the result
cv.imwrite('blended_result.jpg', blended_image)
