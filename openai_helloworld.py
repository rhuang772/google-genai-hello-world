import google.generativeai as genai

# configure your api key here
genai.configure(api_key="AIzaSyBYuDV_1MtL-E3IMxoiQyBhoA7PWPgm6x8")

# initialize the model
model = genai.GenerativeModel('gemini-pro')

# ask the model to generate content
response = model.generate_content("Reply with 'Hello World! How are you?'")
print(response.text) 