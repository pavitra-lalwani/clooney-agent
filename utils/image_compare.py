"""
Image comparison for fidelity scoring
"""

from pathlib import Path
from typing import Tuple
from PIL import Image
import numpy as np
from skimage.metrics import structural_similarity as ssim

class ImageComparator:
    """Compare images for visual fidelity scoring"""
    
    @staticmethod
    def calculate_ssim(image1_path: str, image2_path: str) -> float:
        """Calculate structural similarity index"""
        img1 = Image.open(image1_path).convert('RGB')
        img2 = Image.open(image2_path).convert('RGB')
        
        # Resize to same dimensions if needed
        if img1.size != img2.size:
            img2 = img2.resize(img1.size, Image.LANCZOS)
        
        # Convert to numpy arrays
        arr1 = np.array(img1)
        arr2 = np.array(img2)
        
        # Calculate SSIM
        score = ssim(arr1, arr2, channel_axis=2, data_range=255)
        return float(score)
    
    @staticmethod
    def calculate_pixel_difference(image1_path: str, image2_path: str) -> float:
        """Calculate percentage of different pixels"""
        img1 = Image.open(image1_path).convert('RGB')
        img2 = Image.open(image2_path).convert('RGB')
        
        if img1.size != img2.size:
            img2 = img2.resize(img1.size, Image.LANCZOS)
        
        arr1 = np.array(img1)
        arr2 = np.array(img2)
        
        # Calculate difference
        diff = np.abs(arr1 - arr2)
        different_pixels = np.sum(diff > 10)  # Threshold of 10
        total_pixels = arr1.size
        
        return 1.0 - (different_pixels / total_pixels)
    
    @staticmethod
    def generate_diff_image(image1_path: str, image2_path: str, output_path: str):
        """Generate difference image highlighting changes"""
        img1 = Image.open(image1_path).convert('RGB')
        img2 = Image.open(image2_path).convert('RGB')
        
        if img1.size != img2.size:
            img2 = img2.resize(img1.size, Image.LANCZOS)
        
        arr1 = np.array(img1)
        arr2 = np.array(img2)
        
        # Calculate absolute difference
        diff = np.abs(arr1 - arr2)
        
        # Amplify differences for visibility
        diff = np.clip(diff * 5, 0, 255).astype(np.uint8)
        
        diff_img = Image.fromarray(diff)
        diff_img.save(output_path)