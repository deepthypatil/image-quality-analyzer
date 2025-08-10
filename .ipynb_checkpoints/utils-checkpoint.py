import cv2
import numpy as np

def calc_blurriness(img):
    """Measure blurriness using variance of Laplacian."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return cv2.Laplacian(gray, cv2.CV_64F).var()

def calc_brightness(img):
    """Measure brightness using mean of V channel in HSV."""
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return hsv[:, :, 2].mean()

def calc_contrast(img):
    """Measure contrast as standard deviation of grayscale."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray.std()

def calc_noise(img):
    """Estimate noise as mean absolute difference from Gaussian blur."""
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (3, 3), 0)
    return np.mean(np.abs(gray - blur))

def calc_resolution(img):
    """Return total number of pixels (width × height)."""
    h, w = img.shape[:2]
    return w * h
