import requests
from langchain_community.document_loaders import PyPDFLoader

# Step 1: Download the PDF from the given link
def download_pdf(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            file.write(response.content)
        print(f"PDF downloaded and saved to {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

# Step 2: Specify the URL and download the file
pdf_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/WgM1DaUn2SYPcCg_It57tA/A-Comprehensive-Review-of-Low-Rank-Adaptation-in-Large-Language-Models-for-Efficient-Parameter-Tuning-1.pdf"
pdf_path = "paper.pdf"
download_pdf(pdf_url, pdf_path)

# Step 3: Load the PDF and extract content
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Step 4: Print the first 1000 characters
print("First 1000 characters of the document:")
print(documents[0].page_content[:1000])