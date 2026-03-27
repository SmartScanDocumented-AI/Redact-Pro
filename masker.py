import easyocr
import re
from utils import mask_pii  # Importing your updated utility function

# Initialize EasyOCR once at the top level to save memory/time
# 'en' for English; add 'hi' if you are scanning Hindi documents
reader = easyocr.Reader(['en'])

def extract_text(image_path):
    """Uses EasyOCR to get text and bounding boxes."""
    results = reader.readtext(image_path)
    return results

def detect_pii(ocr_results):
    """
    Analyzes OCR text and returns bounding boxes of sensitive data.
    """
    pii_boxes = []

    # Regex patterns
    # Aadhaar: Handles 12 digits or 4-digit chunks with spaces/dashes
    aadhar_pattern = r'\d{4}[\s-]?\d{4}[\s-]?\d{4}'
    # Email: Standard format
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # Phone: 10 digits, optional +91 prefix
    phone_pattern = r'(\+91[\s-]?|0)?[6-9]\d{9}'
    # PAN Card: 5 letters, 4 numbers, 1 letter
    pan_pattern = r'[A-Z]{5}[0-9]{4}[A-Z]'

    for bbox, text, conf in ocr_results:
        # Pre-process text for matching (remove spaces, fix common OCR swaps)
        original_text = text.strip()
        clean_text = original_text.upper().replace(" ", "").replace("-", "")
        # Fix common OCR mistakes: O -> 0, I -> 1
        clean_text = clean_text.replace("O", "0").replace("I", "1")

        # 1. Check for Aadhaar (12 digits)
        if re.fullmatch(r'\d{12}', clean_text):
            pii_boxes.append(bbox)
        
        # 2. Check for Aadhaar chunks (4 digits) - optional, use carefully
        elif len(clean_text) == 4 and clean_text.isdigit():
            pii_boxes.append(bbox)

        # 3. Check for PAN Card
        elif re.fullmatch(pan_pattern, clean_text):
            pii_boxes.append(bbox)

        # 4. Check for Phone Number
        elif re.search(r'[6-9]\d{9}', clean_text):
            pii_boxes.append(bbox)

        # 5. Check for Email (using original text to keep case/special chars)
        elif re.search(email_pattern, original_text.lower()):
            pii_boxes.append(bbox)

    return pii_boxes

def process_image(image_path, mode="black"):
    """
    The main function called by app.py.
    1. Extracts text
    2. Detects PII
    3. Calls utils.py to apply the mask
    """
    # Step 1: Get OCR results
    ocr_results = extract_text(image_path)
    
    # Step 2: Identify which boxes contain sensitive info
    pii_boxes = detect_pii(ocr_results)
    
    # Step 3: Use utils.py to draw the masks (black, blur, etc.)
    masked_image_path = mask_pii(image_path, pii_boxes, mode)
    
    return masked_image_path

if __name__ == "__main__":
    print("Masker module loaded. Use process_image() to begin.")