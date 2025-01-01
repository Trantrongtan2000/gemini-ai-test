import google.generativeai as genai
import time
import csv

GOOGLE_API_KEY = "AIzaSyDTyMSAO4W5-TUef4rtaAdm3J_4vU_LhT8" # Please set your API key.
pdf_file = "Scan_nha khoa.pdf" # Please set your PDF file with the path.
name = "sample-name-2"

genai.configure(api_key=GOOGLE_API_KEY)

# Check uploaded file.
try:
    pdfFile = genai.get_file(f"files/{name}")
    print(f"File URI: {pdfFile.uri}")
except:
    print(f"Uploading file...")
    pdfFile = genai.upload_file(path=pdf_file, name=name, resumable=True)
    print(f"Completed upload: {pdfFile.uri}")

# Check the state of the uploaded file.
while pdfFile.state.name == "PROCESSING":
    print(".", end="")
    time.sleep(10)
    pdfFile = genai.get_file(pdfFile.name)

if pdfFile.state.name == "FAILED":
    raise ValueError(pdfFile.state.name)

# model_name="gemini-1.5-pro",
# Generate content using the uploaded file.
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-thinking-exp-1219",
    system_instruction=[
        "Bạn là người phân tích chuyên nghiệp, có thể phân tích chính xác văn bản từ hình ảnh và PDF.",
        "Nhiệm vụ của bạn là sao chép văn bản từ tệp PDF được cung cấp.",
    ],
)
prompt = "Chỉ lấy theo dạng file csv với nội dung Tên Thiết Bị, model, hãng (nếu có), nước sản xuất (nếu có), đơn vị tính, Số lượng, Chú thích hoặc S/N hoặc số seri, Số hợp đồng hoặc số đề xuất."
print("Making LLM inference request...")
response = model.generate_content([pdfFile, prompt], request_options={"timeout": 1200})
print(response.text)

print("Saving response to csv file...")


# Parse the response text to extract the CSV content
csv_content = response.text.strip().split('\n')

# Define the CSV file path
csv_file_path = "output7.csv"

# Write the CSV content to a file
with open(csv_file_path, mode='w', newline='', encoding='utf-8-sig') as csv_file:
    writer = csv.writer(csv_file)
    for row in csv_content:
        writer.writerow(row.split(','))

print(f"CSV file saved to {csv_file_path}")