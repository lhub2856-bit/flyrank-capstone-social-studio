from PIL import Image
import os

def generate_image_variants(source_image_path: str, output_dir: str = "output_images"):
    os.makedirs(output_dir, exist_ok=True)
    
    try:
        img = Image.open(source_image_path)
    except FileNotFoundError:
        print(f"Source image not found at {source_image_path}. Using a blank placeholder.")
        # Create a placeholder image if source doesn't exist
        img = Image.new('RGB', (2000, 2000), color=(73, 109, 137))
    
    # 1. Instagram Variant (Square 1080x1080)
    insta_size = (1080, 1080)
    insta_img = img.resize(insta_size, Image.Resampling.LANCZOS)
    insta_path = os.path.join(output_dir, "instagram_variant.jpg")
    insta_img.save(insta_path, "JPEG")
    
    # 2. X (Twitter) Variant (Landscape 1600x900)[cite: 1]
    x_size = (1600, 900)
    x_img = img.resize(x_size, Image.Resampling.LANCZOS)
    x_path = os.path.join(output_dir, "x_variant.jpg")
    x_img.save(x_path, "JPEG")
    
    print(f"Variants generated successfully in {output_dir}/")
    return {"instagram": insta_path, "x": x_path}