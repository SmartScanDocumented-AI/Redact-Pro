# Redact-Pro

SmartScan - Automated PII masking System
Protecting Sensitive Data Using AI

---

## Project Title

**SmartScan: AI-Based Automated Document PII Masker**

---

## Problem Statement

In today's digital world, documents containing sensitive information such as Aadhaar numbers are frequently shared online.This creates serious risks including identity theft,data breaches, and privacy violations.

Manual masking of such data is:

- Time-consuming
- Error-prone
- Not scalable

There is a need for an automated system that can detect and hide sensitive information efficiently.

---

## Solution

SmartScan is a web-based application that automatically detects and masks Personally Identifiable Information (PII) from images.

The system uses AI and image processing techniques to:

- Extract text from images
- Identify sensitive data patterns
- Mask detected information automatically

### Key Features

- Upload image through web interface
- Detect Aadhaar numbers and Email IDs
- Automatically mask sensitive information
- Download secure masked image
- Fast and user-friendly system

---

## Tech Stack

## Backend:

- Python
- Flask

### AI & Processing:

- EasyOCR - Text extraction from images
- OpenCV - Image processing and masking
- Regex - pattern detection

### Frontend:

- HTML
- CSS
- Tailwind CSS

### Tools:

- Git & GitHub

---

## Architecture Flow

### Frontend (User Interface Layer)

The Frontend provides an interactive interface where users can upload images and view results. It includes features like drag-and-drop upload, processing indicators, and result display.

---

### Backend (Application Layer)

The backend is built using Flask and handles:

- Receiving uploaded images
- Storing files in the server
- Sending images to the AI processing module
- Returning masked images to the user

---

### AI Processing Engine (Core Logic Layer)

This is the core component where:

- Text is extracted using OCR
- Sensitive data is detected using Regex
- Detected regions are masked using OpenCV

---

## Workflow:

1. User uploads image via frontend
2. Backend receives and stores the image
3. Image is processed using OCR
4. Sensitive data is detected using Regex
5. OpenCV masks the detected regions
6. Masked image is sent back to the user

---

## Testing

The system was tested using multiple scenarios:

- Images containing Aadhaar numbers
- Images with email IDs
- Multiple sensitive data in a single image
- Low-quality and slightly blurred images

### Results:

- Accurate detection of Aadhaar numbers and emails
- Proper masking of detected regions
- Efficient performance for standard images

---

## Future Scope

- Detection of additional
  - PAN card numbers
  - Phone numbers
  - Passport details

- Support for PDF document masking
- Multi-Language OCR support
- Real-time video masking
- Integration with enterprise systems(banks, hospitals, government, platforms)

## Team contributions

- **Member 1:** Backend Development (Flask Integration)
- **Member 2:** AI Engine (OCR +Masking Logic)
- **Member 3:** Frontend UI/UX Design
- **Member 4:** Testing,Documentation and Presentation

---

## Conclusion

SmartScan provides a fast, reliable, and scalable solution to protect sensitive information in digital documents, By combining AI and image processing, it ensures secure data sharing and reduces the risk of privacy breaches.

---

# Protect Data. Protect Identity