import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import io

def add_na_page_to_pdfs_in_dir(directory):
    # Create a new PDF with "NA" written on it to use as the additional page
    packet = io.BytesIO()
    c = canvas.Canvas(packet, pagesize=letter)
    c.drawString(100, 500, "NA")  # Position the "NA" on the page
    c.save()
    packet.seek(0)
    new_pdf = PdfReader(packet)

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            output_path = os.path.join(directory, "mod", f"{filename}")


            # Read the existing PDF
            reader = PdfReader(pdf_path)
            writer = PdfWriter()

            # Copy existing pages to the writer
            for page in reader.pages:
                writer.add_page(page)

            # Add the "NA" page to the end
            writer.add_page(new_pdf.pages[0])

            # Write the modified content to a new file with the "mod_" prefix
            with open(output_path, 'wb') as out_file:
                writer.write(out_file)

            print(f"Modified file saved as: {output_path}")

# Call the function with the current directory
current_directory = '.'
add_na_page_to_pdfs_in_dir(current_directory)

