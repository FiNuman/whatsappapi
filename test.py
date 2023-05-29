from flask import Flask, request
import requests
 
app = Flask(__name__)
 
# Set the environment variables for the WhatsApp and Google API keys.
WHATSAPP_API_KEY = 'AIzaSyAIPp0KV-wBZZD-qb95axW2QFGi5HQu78s'
GOOGLE_API_KEY = '83Lsxh2R7ZJB2T7hDNm1VXInAK'
 
@app.route("/")
def index():
    return "Hello, World! xxx"
 
# @app.route("/get_bard_response/<string:text>")
# def get_bard_response(text):
#     response = requests.post(
#         "https://api.bard.ai/v2/generate",
#         headers={
#             "Authorization": f"Bearer 83Lsxh2R7ZJB2T7hDNm1VXInAK"
#         },
#         data={
#             "text": 'text'
#         }
#     )
#     response.raise_for_status()
#     return response.json({numan:'dasd'})
 
# @app.route("/generate_voice_audio/<string:text>")
# def generate_voice_audio(text):
#     response = get_bard_response(text)
#     voice_url = response["data"]["voice_url"]
#     return voice_url
 
  
# @app.route("/get_audio/<string:word>/<string:accent>")
# def get_audio(word, accent):
#     pronunciation = get_pronunciation(word, accent)
#     voice_url = generate_voice_audio(pronunciation)
#     return voice_url
 
# @app.route("/send_message/<chat_id>/<message>")
# def send_message(chat_id, message):
#     requests.post(
#         f"https://api.whatsapp.com/v1/send/?chat_id={chat_id}&text={message}",
#         headers={
#             "Authorization": f"Bearer AIzaSyAIPp0KV-wBZZD-qb95axW2QFGi5HQu78s"
#         }
#     )
 
#     # Respond to the user.
#     return "I heard you say: " 'ok response'
 
if __name__ == "__main__":
    app.run(debug=True)