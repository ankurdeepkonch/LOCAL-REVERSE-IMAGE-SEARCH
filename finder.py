from PIL import Image
import imagehash
import os

# --- DESIGNS PICS FOLDER ---
designs_folder = r"E:\PROJECT_FILES\DESIGNS"

# Your first screenshot folder
screenshots_folder_1 = r"E:\DOWNLOADS"

# Your second screenshot folder 
screenshots_folder_2 = r"E:\SCREENSHOTS" 


def find_matching_design():
    # Ask you for the name of the screenshot
    screenshot_name = input("Enter the exact name of the screenshot (e.g., test1.jpg): ")
    
    # First, try to find it in Folder 1
    screenshot_path = os.path.join(screenshots_folder_1, screenshot_name)
    
    # If it is NOT in Folder 1, try Folder 2 instead
    if not os.path.exists(screenshot_path):
        screenshot_path = os.path.join(screenshots_folder_2, screenshot_name)
        
    # If it is still not found in either folder, print an error
    if not os.path.exists(screenshot_path):
        print(f"Error: Could not find '{screenshot_name}' in either folder.")
        return

    print(f"Found it! Analyzing {screenshot_name}...")
    screenshot_hash = imagehash.average_hash(Image.open(screenshot_path))
    
    best_match = None
    smallest_difference = 100 
    
    print(f"Scanning your design library in {designs_folder}...")
    for filename in os.listdir(designs_folder):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            design_path = os.path.join(designs_folder, filename)
            
            try:
                design_hash = imagehash.average_hash(Image.open(design_path))
                difference = screenshot_hash - design_hash
                
                # A smaller difference means a closer visual match
                if difference < smallest_difference:
                    smallest_difference = difference
                    best_match = filename
                    
            except Exception:
                pass # Skips any broken files silently

    print("-" * 40)
    if best_match:
        print(f"SUCCESS! The closest match is: {best_match}")
    else:
        print("Could not find any matching search again images.")

if __name__ == "__main__":
    find_matching_design()

    