import PyPDF2
import docx

def extract_txt(file_path):
    text=""
    if file_path.endswith('.pdf'):
        with open(file_path, 'rb') as file:
            reader= PyPDF2.PdfReader(file)
            for page in reader.pages:
                page_txt=page.extract_text()
                if page_txt:
                    text+=page_txt
    elif file_path.endswith('.docx'):
        doc=docx.Document(file_path)
        for para in doc.paragraphs:
            text+=para.text
    else:
        raise ValueError("Unsupported file format. Please upload a PDF or DOCX file.")
    return text.strip()