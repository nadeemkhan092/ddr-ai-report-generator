import fitz
import os

def extract_text(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

def extract_images(pdf_path, output_folder):
    doc = fitz.open(pdf_path)
    os.makedirs(output_folder, exist_ok=True)

    image_paths = []

    for i, page in enumerate(doc):
        for j, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            path = f"{output_folder}/img_{i}_{j}.png"
            with open(path, "wb") as f:
                f.write(image_bytes)

            image_paths.append(path)

    return image_paths
