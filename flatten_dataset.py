import os
import shutil

def flatten_folder_structure(main_folder):
    for category in ["good", "bad"]:
        category_path = os.path.join(main_folder, category)
        for root, dirs, files in os.walk(category_path):
            for file in files:
                src = os.path.join(root, file)
                dst = os.path.join(category_path, file)
                # Avoid overwriting if filenames repeat
                if not os.path.exists(dst):
                    shutil.move(src, dst)

# Change this to your dataset directory
base_dir = r"D:\projects\image_quality_analyzer\data"
flatten_folder_structure(base_dir)
print("✅ All images moved to top-level good/bad folders")
