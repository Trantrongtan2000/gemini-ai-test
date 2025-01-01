import os

def get_pdf_files(directory):
    pdf_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def rename_files(files):
    for file in files:
        new_file = os.path.join(os.path.dirname(file), os.path.basename(file).replace('_', '-'))
        os.rename(file, new_file)

directory = 'C:/Users/Admin/Desktop/ai-test'
pdf_files = get_pdf_files(directory)
rename_files(pdf_files)

for pdf in pdf_files:
    print(pdf.replace('_', '-'))