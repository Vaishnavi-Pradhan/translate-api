# from googletrans import Translator
# #https://py-googletrans.readthedocs.io/en/latest/    ==> for language codes
# translater = Translator()
# text = "YOu are the only one i trust the most"
# out = translater.translate(text,dest="mr")
# print(out.text)


from flask import Flask, request, jsonify
from googletrans import Translator
from flask_cors import CORS
import os  # Import os to get Render's assigned port

app = Flask(__name__)
CORS(app)  # Allows cross-origin requests (React Native needs this)

translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_text():
    try:
        data = request.get_json()
        text = data.get("text")
        lang = data.get("lang")

        if not text or not lang:
            return jsonify({"error": "Text and language code are required"}), 400

        translated_text = translator.translate(text, dest=lang).text
        return jsonify({"translated_text": translated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render assigns a dynamic port
    app.run(host='0.0.0.0', port=port, debug=True)
