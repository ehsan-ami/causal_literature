import requests
import glob
import os

# Define your API key and headers
api_key = 'ask_f62650ba5509fc91587a4f7a87af0823'
headers = {
    'x-api-key': api_key
}

# Define the directory containing your PDF files
pdf_directory = '/Users/ehsan/papers/mod'

# Get a list of all PDF files in the directory
pdf_files = glob.glob(os.path.join(pdf_directory, '*.pdf'))

# Function to upload a single file
def upload_pdf(file_path):
    with open(file_path, 'rb') as file_data:
        response = requests.post('https://api.askyourpdf.com/v1/api/upload', headers=headers, files={'file': file_data})
        if response.status_code == 201:
            print(f"Successfully uploaded {os.path.basename(file_path)}: {response.json()}")
        else:
            print(f"Error {response.status_code} while uploading {os.path.basename(file_path)}")

# Iterate through the PDF files and upload each one
for pdf_file in pdf_files:
    upload_pdf(pdf_file)
