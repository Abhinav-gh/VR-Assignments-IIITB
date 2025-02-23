# Image Stitching using Feature Matching & Homography

This project implements an image stitching pipeline using **SIFT-based feature detection**, **homography estimation**, and **gradient blending**. The goal is to create a seamless panorama from multiple images.

## Features

- Detects keypoints using **SIFT (Scale-Invariant Feature Transform)**
- Matches features between images
- Computes **homography transformation** using **RANSAC**
- Warps images to a common coordinate space
- Uses **gradient blending** for smooth transitions
- Supports **multiple image stitching** iteratively

## 📂 Dataset

You can use any set of overlapping images for testing. This implementation was tested on **high-resolution images** captured on a mobile device.

## 🚀 Installation

1. **Clone the repository:**

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
jupyter notebook Coin_Detection_Segmentation_Counting.ipynb
jupyter notebook img_stitching.ipynb
```
