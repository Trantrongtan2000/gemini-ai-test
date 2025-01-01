import google.generativeai as genai
import time
import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import unicodedata

GOOGLE_API_KEY = "AIzaSyDTyMSAO4W5-TUef4rtaAdm3J_4vU_LhT8"  # Please set your API key.

genai.configure(api_key=GOOGLE_API_KEY)

def log_message(message):
    log_text.insert(tk.END, message + "\n")
    log_text.see(tk.END)
'''
def process_pdf(pdf_file):
    original_name = pdf_file.split('/')[-1].split('.')[0]
    name = original_name.lower().replace(' ', '-').replace('_', '-')
    name = ''.join(c for c in name if c.isalnum() or c == '-')
    name = name.strip('-')
    while name.startswith('-') or name.endswith('-'):
        name = name.strip('-')
    if not name:
        raise ValueError("File name cannot be empty after formatting.")
    if not name[0].isalnum():
        name = 'a' + name
    if not name[-1].isalnum():
        name = name + 'a'

    log_message(f"Processing file: {pdf_file}")

    # Check uploaded file.
    try:
        pdfFile = genai.get_file(f"files/{name}")
        log_message(f"File URI: {pdfFile.uri}")
    except:
        log_message(f"Uploading file...")
        pdfFile = genai.upload_file(path=pdf_file, name=name, resumable=True)
        log_message(f"Completed upload: {pdfFile.uri}")

    # Check the state of the uploaded file.
    while pdfFile.state.name == "PROCESSING":
        log_message("Processing...")
        time.sleep(10)
        pdfFile = genai.get_file(pdfFile.name)

    if pdfFile.state.name == "FAILED":
        raise ValueError(pdfFile.state.name)

    # Generate content using the uploaded file.
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-thinking-exp-1219",
        system_instruction=[
            "Bạn là người phân tích chuyên nghiệp, có thể phân tích chính xác văn bản từ hình ảnh và PDF.",
            "Nhiệm vụ của bạn là sao chép văn bản từ tệp PDF được cung cấp.",
        ],
    )
    prompt = "Chỉ lấy theo dạng file csv với nội dung Tên Thiết Bị, model, hãng (nếu có), nước sản xuất (nếu có), đơn vị tính, Số lượng, Chú thích hoặc S/N hoặc số seri, Số hợp đồng hoặc số đề xuất."
    log_message("Making LLM inference request...")
    response = model.generate_content([pdfFile, prompt], request_options={"timeout": 1200})
    log_message("LLM inference request completed.")

    log_message("Saving response to csv file...")

    # Parse the response text to extract the CSV content
    csv_content = response.text.strip().split('\n')

    # Define the CSV file path
    csv_file_path = f"{original_name}.csv"

    # Write the CSV content to a file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        for row in csv_content:
            writer.writerow(row.split(','))

    log_message(f"CSV file saved to {csv_file_path}")
    messagebox.showinfo("Success", f"CSV file saved to {csv_file_path}")
'''

def process_pdf(pdf_file):
    original_name = pdf_file.split('/')[-1].split('.')[0]
    name = remove_accents(original_name.lower().replace(' ', '-').replace('_', '-'))
    name = ''.join(c for c in name if c.isalnum() or c == '-')
    name = name.strip('-')
    while name.startswith('-') or name.endswith('-'):
        name = name.strip('-')
    if not name:
        raise ValueError("File name cannot be empty after formatting.")
    if not name[0].isalnum():
        name = 'a' + name
    if not name[-1].isalnum():
        name = name + 'a'

    log_message(f"Processing file: {pdf_file}")
    root.update_idletasks()  # Update the GUI to show the log message immediately

    # Check uploaded file.
    try:
        pdfFile = genai.get_file(f"files/{name}")
        log_message(f"File URI: {pdfFile.uri}")
        root.update_idletasks()
    except:
        log_message(f"Uploading file...")
        root.update_idletasks()
        pdfFile = genai.upload_file(path=pdf_file, name=name, resumable=True)
        log_message(f"Completed upload: {pdfFile.uri}")
        root.update_idletasks()

    # Check the state of the uploaded file.
    while pdfFile.state.name == "PROCESSING":
        log_message("Processing...")
        root.update_idletasks()
        time.sleep(10)
        pdfFile = genai.get_file(pdfFile.name)

    if pdfFile.state.name == "FAILED":
        raise ValueError(pdfFile.state.name)

    # Generate content using the uploaded file.
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-thinking-exp-1219",
        system_instruction=[
            "Bạn là người phân tích chuyên nghiệp, có thể phân tích chính xác văn bản từ hình ảnh và PDF.",
            "Nhiệm vụ của bạn là sao chép văn bản từ tệp PDF được cung cấp.",
        ],
    )
    prompt = "Chỉ lấy theo dạng file csv với nội dung Tên Thiết Bị, model, hãng (nếu có), nước sản xuất (nếu có), đơn vị tính, Số lượng, Chú thích hoặc S/N hoặc số seri, Số hợp đồng hoặc số đề xuất."
    log_message("Making LLM inference request...")
    root.update_idletasks()
    response = model.generate_content([pdfFile, prompt], request_options={"timeout": 1200})
    log_message("LLM inference request completed.")
    root.update_idletasks()

    log_message("Saving response to csv file...")
    root.update_idletasks()

    # Parse the response text to extract the CSV content
    csv_content = response.text.strip().split('\n')

    # Define the CSV file path
    csv_file_path = f"{original_name}.csv"

    # Write the CSV content to a file
    with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
        writer = csv.writer(csv_file)
        for row in csv_content:
            writer.writerow(row.split(','))

    log_message(f"CSV file saved to {csv_file_path}")
    root.update_idletasks()
    # messagebox.showinfo("Success", f"CSV file saved to {csv_file_path}")

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        process_pdf(file_path)

# Create the main window
root = tk.Tk()
root.title("Chuyển đổi biên bản bàn giao từ PDF sang CSV bằng Gemini AI")

log_text = tk.Text(root, height=1, width=50)
log_text.insert(tk.END, ' Chọn tệp và AI sẽ xử lý')
log_text.pack(pady=10)

# Create a text widget to display logs
log_text = tk.Text(root, height=10, width=50)
log_text.pack(pady=10)

# Create a button to select the PDF file
select_button = tk.Button(root, text="Chọn file PDF", command=select_file)
select_button.pack(pady=10)

# Create an exit button to close the application
exit_button = tk.Button(root, text="Exit", command=root.quit)
exit_button.pack(pady=10)

# Run the application
root.mainloop()


