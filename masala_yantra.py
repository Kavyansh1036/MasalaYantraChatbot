import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

system_prompt = """You are MasalaYantra, a purely culinary AI assistant specializing in:
- Indian recipes and cooking techniques
- Spice combinations and their uses
- Kitchen tips and food preparation
- Cultural context of Indian dishes

You strictly avoid:
- Any non-culinary topics
- Personal/relationship discussions
- Medical/health advice
- Offensive content

Style:
- Warm and grandmotherly
- Patient with beginners
- Culturally respectful
"""

def get_masala_response(user_input):
    try:
        chat = model.start_chat(history=[])
        
        response = chat.send_message(
            system_prompt + "\nUser: " + user_input,
            safety_settings={
                'HARM_CATEGORY_HARASSMENT': 'BLOCK_ONLY_HIGH',
                'HARM_CATEGORY_HATE_SPEECH': 'BLOCK_ONLY_HIGH',
                'HARM_CATEGORY_SEXUALLY_EXPLICIT': 'BLOCK_ONLY_HIGH',
                'HARM_CATEGORY_DANGEROUS_CONTENT': 'BLOCK_ONLY_HIGH'
            },
            generation_config={
                'temperature': 0.5,
                'top_p': 0.95,
                'top_k': 40,
                'max_output_tokens': 1024
            }
        )
        return response.text
    except Exception as e:
        if "sexual_content" in str(e):
            return "Namaste! Let's keep our conversation focused on Indian cooking. How can I help you with recipes or spices today?"
        return "Namaste! 🙏 Please ask me about Indian cooking, spices, or recipes."