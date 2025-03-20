import cv2
import pytesseract
from pytesseract import Output

# Function to extract text from image
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, output_type=Output.STRING)
    return text

# Function to compare extracted text with accessibility guidelines
def compare_with_guidelines(extracted_text):
    guidelines = {
        "font_size": 12,
        "contrast_ratio": 4.5,
        "alt_text": True
    }
    
    results = {
        "font_size": "Pass" if len(extracted_text) > guidelines["font_size"] else "Fail",
        "contrast_ratio": "Pass" if len(extracted_text) > guidelines["contrast_ratio"] else "Fail",
        "alt_text": "Pass" if guidelines["alt_text"] else "Fail"
    }
    
    return results

# Function to create comparison result
def create_comparison_result(image_path):
    extracted_text = extract_text_from_image(image_path)
    results = compare_with_guidelines(extracted_text)
    
    print("Accessibility Assessment Results:")
    for key, value in results.items():
        print(f"{key}: {value}")

# Main function
if __name__ == "__main__":
    image_path = "path_to_your_image_file.png"
    create_comparison_result(image_path)