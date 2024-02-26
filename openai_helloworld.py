import google.generativeai as genai

genai.configure(api_key="AIzaSyBYuDV_1MtL-E3IMxoiQyBhoA7PWPgm6x8")

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Reply with 'Hello World! How are you?' ")
print(response.text) 