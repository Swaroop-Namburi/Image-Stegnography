# 🕵️‍♂️ Image Steganography GUI using Python

A simple GUI-based application to hide and reveal secret messages within image files using the Least Significant Bit (LSB) method. Built with Python, Tkinter, and Stegano.

## 🖼️ Features

- Hide secret messages in images
- Protect messages using a secret key
- Reveal hidden messages with proper authentication
- GUI interface for ease of use
- Supports PNG, JPG, and JPEG formats

## 🔧 Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## 📦 Technologies Used

- Python 3.x
- Tkinter (Standard Library)
- Pillow (for image processing)
- Stegano (for LSB steganography)

## 🚀 How to Use

1. Clone the repository or download the source code.
2. Run the Python script:

   ```bash
   python steganography_gui.py
   ```

3. Follow these steps in the GUI:
   - **Open Image**: Choose a `.png`, `.jpg`, or `.jpeg` file.
   - **Enter Text**: Type the message you want to hide.
   - **Enter Secret Key**: Provide a key to encrypt the message.
   - **Hide Text**: Hide the message inside the image.
   - **Save Image**: Save the modified image.
   - To reveal:
     - Open the saved image (`Secret File.png`)
     - Enter the correct secret key
     - Click "Show Data"

## 📂 File Structure

```
.
├── steganography_gui.py      # Main application script
├── requirements.txt          # Dependencies
└── README.md                 # Project description
```

## ⚠️ Notes

- The secret key should be between 1 to 9 characters.
- Make sure the original image is in RGB mode (automatic conversion is handled).

## 🛡️ License

This project is open-source and available under the [MIT License](LICENSE).

---

> Built with ❤️ in Python
