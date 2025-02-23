# 🖼️ Image Stitching & Coin Detection, Segmentation, and Counting

This project implements two major computer vision tasks:

1. **Image Stitching using Feature Matching & Homography**  
   - **SIFT-based feature detection** for identifying key points.  
   - **Homography estimation** to align images into a common coordinate space.  
   - **Gradient blending** for seamless transitions between stitched images.  
   - **Application to high-resolution images**, including real-world datasets.  

2. **Coin Detection, Segmentation, and Counting**  
   - **Preprocessing with edge detection (Canny) and thresholding**.  
   - **Contour-based segmentation** to detect and isolate coins.  
   - **Morphological operations** for noise removal and refinement.  
   - **Counting the number of coins** in an image.  

This project explores how feature-based stitching and image segmentation techniques can be applied to real-world problems effectively.


## 🚀 Features

### 🔹 Image Stitching
- Detects keypoints using **SIFT (Scale-Invariant Feature Transform)**  
- Matches features between images using **FLANN-based matcher**  
- Computes **homography transformation** using **RANSAC**  
- Warps images to a common coordinate space for alignment  
- Uses **gradient blending** for smooth transitions  
- Supports **multiple image stitching** iteratively  

### 🔹 Coin Detection & Counting
- Applies **Canny edge detection** and **thresholding** for preprocessing  
- Uses **contour-based segmentation** to detect and isolate coins  
- Employs **morphological operations** for noise removal  
- Counts the number of detected coins accurately  
- Works with **Indian coins** and can be extended to other currencies  


## 📂 Dataset

This implementation was tested on:
- **High-resolution images** of our institute, captured using a mobile phone  
- **Publicly available images** from the internet for benchmarking  
- **Indian coin images** for the coin detection and counting task  

You can use any set of overlapping images or coin images for testing.


## 🚀 Installation

1. **Clone the repository:**
```bash
git clone git@github.com:Abhinav-gh/VR-Assignments-IIITB.git

cd VR-Assignments-IIITB
```
2. **Create a conda environment (recommended):**
   
```sh
conda create -n image_stitching python=3.8  # Or your preferred Python version
conda activate image_stitching
```
3. **Install dependencies:**
```sh
pip install -r requirements.txt
```
4. Run the notebooks:
```sh
jupyter notebook Coin Detection_Segmentation_counting.ipynb
jupyter notebook Img stitching.ipynb
```

## 📚 Documentation
The `DOCS/` directory contains a detailed LaTeX report covering:

- **Introduction**: Overview of the project, objectives, and methodology.
- **Feature Detection & Matching**: Use of SIFT for keypoint detection and FLANN for feature matching.
- **Homography Estimation**: Explanation of RANSAC-based homography computation.
- **Image Warping & Stitching**: Transforming and aligning images using the estimated homography.
- **Blending Techniques**: Comparison of gradient blending and weighted blending for smooth image transitions.
- **Results on High-Resolution Images**: Application of the method on images captured from our institute.
- **Coin Detection, Segmentation, and Counting**: Using computer vision techniques to detect, segment, and count Indian coins.
- **Conclusion**: Summary of work done

Example outputs and figures are also included in the report.

## ✒️ Authors

- **Abhinav Deshpande**  [GitHub](https://github.com/Abhinav-gh)






