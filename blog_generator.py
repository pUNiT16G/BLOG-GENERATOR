import google.generativeai as genai

from dotenv import dotenv_values

# Load API key from .env
config = dotenv_values('.env')
genai.configure(api_key=config["GEMINI_API_KEY"])

# Pick Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_blog(paragraph_topic):
    response = model.generate_content(
        f"Write a paragraph about the following topic: {paragraph_topic}"
    )
    return response.text.strip()

keep_writing = True

while keep_writing:
    answer = input('Write a paragraph? Y for yes, anything else for no: ').strip().lower()
    if answer == 'y':
        paragraph_topic = input('What should this paragraph talk about? ')
        print("\n--- Generated Blog ---\n")
        print(generate_blog(paragraph_topic))
        print("\n----------------------\n")
    else:
        keep_writing = False
      
        ###Enjoy!!!
