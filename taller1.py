import cv2
import numpy as np

def cartoonize(rgb_image: np.ndarray, num_pyr_downs=2, num_bilaterals=7):
    downsampled_img = rgb_image
    for _ in range(num_pyr_downs):
        downsampled_img = cv2.pyrDown(downsampled_img)
    for _ in range(num_bilaterals):
        filterd_small_img = cv2.bilateralFilter(downsampled_img, 9, 9, 7)
    filtered_normal_img = filterd_small_img
    for _ in range(num_pyr_downs):
        filtered_normal_img = cv2.pyrUp(filtered_normal_img)
    if filtered_normal_img.shape != rgb_image.shape:
        filtered_normal_img = cv2.resize(
            filtered_normal_img, rgb_image.shape[:2])

    img_gray = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    gray_edges = cv2.adaptiveThreshold(img_blur, 255,
                                       cv2.ADAPTIVE_THRESH_MEAN_C,
                                       cv2.THRESH_BINARY, 9, 2)

    rgb_edges = cv2.cvtColor(gray_edges, cv2.COLOR_GRAY2RGB)

    return [rgb_image, filtered_normal_img, img_gray, img_blur, gray_edges, cv2.bitwise_and(filtered_normal_img, rgb_edges)]