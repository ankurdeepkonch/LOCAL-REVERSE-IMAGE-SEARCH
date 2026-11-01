# Local Reverse-Image Search

A Python-based visual feature extraction tool built to scan and search through a personal library of over 300 vector design files.

This script allows you to input the name of a screenshot, automatically locates it within your designated download/screenshot folders, and compares its visual hash against a local directory of design files to find the closest visual match.

## Features
* **Average Hashing:** Utilizes the `imagehash` library to extract visual features, allowing it to find matching designs even if the screenshot is slightly cropped, resized, or different in file size.
* **Multi-Folder Checking:** Automatically checks multiple source folders (e.g., Downloads and Screenshots) for your input image.
* **Silent Error Handling:** Automatically skips corrupted or unreadable files in your design library without breaking the scan.

## Prerequisites

Before running the script, make sure you have Python installed along with the required libraries. You can install the dependencies using pip:

```bash
pip install Pillow imagehash
```

## Setup and Configuration

The script uses hardcoded local directory paths. Before running `finder.py` on a different machine, you will need to open the file and update the folder paths to match your local environment:

```python
# --- DESIGNS PICS FOLDER ---
designs_folder = r"E:\PROJECT_FILES\DESIGNS"

# Your first screenshot folder
screenshots_folder_1 = r"E:\DOWNLOADS"

# Your second screenshot folder 
screenshots_folder_2 = r"E:\SCREENSHOTS" 
```

## Usage

1. Open your terminal or command prompt.
2. Run the script:
   ```bash
   python finder.py
   ```
3. When prompted, enter the exact name of the screenshot you want to search for (including the file extension, e.g., `test1.jpg`).
4. The script will locate the screenshot, hash it, and scan your design library to output the filename of the closest match.

## Technologies Used
* **Python 3**
* **Pillow (PIL)** - Image processing
* **ImageHash** - Perceptual image hashing