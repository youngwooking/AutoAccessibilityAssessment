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

def calculate_contrast_ratio(L1, L2):
    L1 = L1 + 0.05
    L2 = L2 + 0.05
    if L1 > L2:
        return L1 / L2
    else:
        return L2 / L1
    
def calculate_relative_luminance(color):
    if any(c < 0 or c > 255 for c in color):
        raise ValueError("Color values should be in the range 0-255")

    if color[0]/255 <= 0.03928:
        R = color[0]/255/12.92
    else:
        R = ((color[0]/255 + 0.055)/1.055)**2.4
    if color[1]/255 <= 0.03928:
        G = color[1]/255/12.92
    else:  
        G = ((color[1]/255 + 0.055)/1.055)**2.4
    if color[2]/255 <= 0.03928:
        B = color[2]/255/12.92
    else:
        B = ((color[2]/255 + 0.055)/1.055)**2.4
        
    return 0.2126 * R + 0.7152 * G + 0.0722 * B



# Main function
if __name__ == "__main__":
    # image_path = "path_to_your_image_file.png"
    # create_comparison_result(image_path)
    print(
        calculate_contrast_ratio(
            calculate_relative_luminance((135, 135, 135)),
            calculate_relative_luminance((1313, 42, 52))
        )
    )