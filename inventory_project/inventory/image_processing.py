import cv2
import pytesseract

def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(gray)

    return text

# Example usage
if __name__ == "__main__":
    image_path = 'path_to_your_image.jpg'
    extracted_text = process_image(image_path)
    print(extracted_text)