

---

```markdown
# Inventory Asset Tracker with OCR

A Django-based web application that lets you upload images of inventory items, automatically extracts text (such as model or serial numbers) using Tesseract OCR, and returns the results. This project serves as the foundation for a more advanced asset management system.

## Features

- **Image Upload:** Users can upload images through a simple form.
- **OCR Extraction:** Uses [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) via `pytesseract` to extract text from images.
- **OpenCV Preprocessing:** Images are preprocessed (e.g., thresholding) for improved OCR accuracy.
- **Future Enhancements:**  
  - **Shape Detection:** Plan to integrate OpenCV shape detection for additional item recognition.
  - **Database Integration:** Store parsed inventory data in Django models.
  - **Mobile Integration:** Capture images via mobile devices and send them to the server.

## Requirements

- **Python 3.7+** (Tested with Python 3.12)
- **Django 5.1+**
- **OpenCV (`opencv-python`)**
- **pytesseract** (Python wrapper for Tesseract)
- **Tesseract OCR Engine**  
  - [Windows builds](https://github.com/UB-Mannheim/tesseract/wiki)
  - Use `brew install tesseract` on macOS
  - Use `sudo apt-get install tesseract-ocr` on Ubuntu/Debian

## Getting Started

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/<YourUsername>/<YourRepoName>.git
   cd <YourRepoName>
   ```

2. **Create & Activate a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *(Alternatively, install each package individually: `pip install django opencv-python pytesseract`.)*

4. **Configure Tesseract:**
   - **Windows:** Download and install from [Tesseract OCR Releases](https://github.com/UB-Mannheim/tesseract/wiki).
   - **macOS:** `brew install tesseract`
   - **Ubuntu/Debian:** `sudo apt-get install tesseract-ocr`

5. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
   Then visit [http://127.0.0.1:8000/upload/](http://127.0.0.1:8000/upload/) to upload an image and see the extracted text.

## Usage

- **Upload Page:** Navigate to `/upload/` in your browser.
- **Upload an Image:** Select a file and submit the form. The system will:
  - Save the file to the `media` folder.
  - Process the image using OCR.
  - Return a JSON response containing the extracted text.
- **Preprocessing:** Modify the `process_image` function in `image_processing.py` to adjust preprocessing for better OCR results if needed.

## Project Structure

```
inventory_project/
├── manage.py
├── inventory_project/           # Project configuration folder
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── inventory/                   # Django app folder
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── image_processing.py
    ├── models.py
    ├── tests.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── upload.html
```

## Future Plans

- **Shape Detection:** Enhance image processing with OpenCV to detect shapes and logos.
- **Database Integration:** Parse extracted text and store inventory details in Django models.
- **Mobile Integration:** Develop a mobile app interface using React Native or Flutter.
- **Deployment:** Deploy the application to a cloud platform like Heroku, AWS, or DigitalOcean.

## Contributing

Contributions, issues, and feature requests are welcome! Please open a pull request or issue in this repository.

## License

This project is licensed under the [MIT License](LICENSE).
```

---

