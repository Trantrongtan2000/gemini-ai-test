import google.generativeai as genai
import os

genai.configure(api_key=("AIzaSyDTyMSAO4W5-TUef4rtaAdm3J_4vU_LhT8"))

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Explain how AI works")
print(response.text)