import os
from PIL import Image

# Configuration
SOURCE_FOLDER = "bgcg"        # Folder with your original images
OUTPUT_FOLDER = "bgcg_thumb"    # Where thumbnails will be saved
THUMBNAIL_SIZE = (256, 256)     # Max width/height
VALID_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".bmp")

def generate_thumbnails():
    # Ensure output folder exists
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    for root, _, files in os.walk(SOURCE_FOLDER):
        for file in files:
            if file.lower().endswith(VALID_EXTENSIONS):
                input_path = os.path.join(root, file)

                # Keep same folder structure in output
                relative_path = os.path.relpath(root, SOURCE_FOLDER)
                output_dir = os.path.join(OUTPUT_FOLDER, relative_path)
                os.makedirs(output_dir, exist_ok=True)

                output_path = os.path.join(output_dir, file)

                try:
                    with Image.open(input_path) as img:
                        img.thumbnail(THUMBNAIL_SIZE)
                        img.save(output_path, optimize=True)
                        print(f"✅ Created thumbnail: {output_path}")
                except Exception as e:
                    print(f"⚠️ Failed to process {input_path}: {e}")

if __name__ == "__main__":
    generate_thumbnails()
    print("\n🎉 Done generating thumbnails!")
