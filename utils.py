import cv2
import os
import numpy as np

def get_box_coordinates(box):
    # Converts EasyOCR bbox to integer coordinates
    # box is usually: [[x,y], [x,y], [x,y], [x,y]]
    top_left, top_right, bottom_right, bottom_left = box
    
    x_min = int(min(top_left[0], bottom_left[0]))
    y_min = int(min(top_left[1], top_right[1]))
    x_max = int(max(top_right[0], bottom_right[0]))
    y_max = int(max(bottom_left[1], bottom_right[1]))
    
    return x_min, y_min, x_max, y_max

def mask_pii(image_path, pii_boxes, mode="black"):
    """
    Masks sensitive info in an image.
    """
    # Create results folder if not exists
    os.makedirs("results", exist_ok=True)

    # Dynamic output path
    base_name = os.path.basename(image_path)
    name, ext = os.path.splitext(base_name)
    output_path = f"results/{name}_masked{ext}"

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image at {image_path}")
        return None

    h, w = image.shape[:2]

    for box in pii_boxes:
        x_min, y_min, x_max, y_max = get_box_coordinates(box)

        # SAFETY: Ensure coordinates are within image boundaries
        x_min, y_min = max(0, x_min), max(0, y_min)
        x_max, y_max = min(w, x_max), min(h, y_max)

        # SAFETY: Skip if the box has no area
        if x_max <= x_min or y_max <= y_min:
            continue

        if mode == "black":
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0,0,0), -1)
            
        elif mode == "blur":
            roi = image[y_min:y_max, x_min:x_max]
            # GaussianBlur kernel size must be odd and > 0
            # If the ROI is too small for a 25x25 blur, we skip or use a smaller kernel
            if roi.shape[0] > 1 and roi.shape[1] > 1:
                roi = cv2.GaussianBlur(roi, (25, 25), 0)
                image[y_min:y_max, x_min:x_max] = roi
                
        elif mode == "highlight":
            cv2.rectangle(image, (x_min, y_min), (x_max, y_max), (0,255,255), 3)

    cv2.imwrite(output_path, image)
    return output_path