import os
import shutil
from docx import Document

def rename_and_create_documents(strings, template_path, output_dir):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Loop through each string
    for index, string in enumerate(strings, start=1):
        new_name = f"Chapter {index} - {string}"
        new_filename = f"{new_name}.docx"
        new_path = os.path.join(output_dir, new_filename)

        # Copy the template document to the new path
        shutil.copy(template_path, new_path)

        # Open the copied document and replace "Template" with the new name
        doc = Document(new_path)
        for paragraph in doc.paragraphs:
            if 'Template' in paragraph.text:
                paragraph.text = paragraph.text.replace('Template', new_name)

        # Save the modified document
        doc.save(new_path)
        print(f"Created: {new_filename}")

# Array of strings
strings = [
    "Introduction",
    "Getting Started",
    "Advanced Techniques",
    "Conclusion"
]

# Path to the template document
template_path = "data/Template - Docs.docx"

# Output directory for the new documents
output_dir = "data/chapters"

# Call the function
rename_and_create_documents(strings, template_path, output_dir)
