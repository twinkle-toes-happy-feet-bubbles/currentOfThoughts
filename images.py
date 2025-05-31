import os
import re
import shutil

# Paths (using raw strings to handle Windows backslashes correctly)
posts_dir = r"C:\Users\prajy\currentofthoughts\content\posts"
attachments_dir = r"C:\Users\prajy\OneDrive\Documents\mindzenspace\Attachments"
static_images_dir = r"C:\Users\prajy\currentofthoughts\static\images"

# Ensure the static images directory exists
os.makedirs(static_images_dir, exist_ok=True)

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # Step 2: Find all image links in the format ![Image Description](/images/Pasted%20image%20...%20.png)
        images = re.findall(r'\[\[([^]]*\.(png|jpg|jpeg|gif|webp))\]\]', content, re.IGNORECASE)

        # Step 3: Replace image links and ensure URLs are correctly formatted
        for image_match in images:
            original_image_name = image_match[0]
            image_extension = image_match[1]
            safe_image_name = original_image_name.replace(' ', '%20')
            markdown_image = f"![{os.path.splitext(original_image_name)[0]}](/images/{safe_image_name})"
            content = content.replace(f"[[{original_image_name}]]", markdown_image)

            # Step 4: Copy the image to the Hugo static/images directory if it exists
            image_source = os.path.join(attachments_dir, original_image_name)
            if os.path.exists(image_source):
                destination_path = os.path.join(static_images_dir, original_image_name)
                try:
                    shutil.copy(image_source, destination_path)
                    print(f"Copied: {original_image_name} to {static_images_dir}")
                except Exception as e:
                    print(f"Error copying {original_image_name}: {e}")
            else:
                print(f"Warning: Image not found in attachments: {original_image_name}")

        # Step 5: Write the updated content back to the markdown file
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("Markdown files processed.")