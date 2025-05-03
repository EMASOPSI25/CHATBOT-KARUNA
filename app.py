from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ganti dengan API key dari Hugging Face
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium"
HEADERS = {
    "Authorization": "Bearer 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"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]

    payload = {
        "inputs": {
            "text": user_message
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    # DEBUG: Lihat isi response
    print("Status:", response.status_code)
    print("Response:", response.text)

    if response.status_code == 200:
        data = response.json()
        reply = data.get("generated_text", "Maaf, tidak ada jawaban.")
    else:
        reply = "Maaf, server sedang sibuk. Coba lagi nanti."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)

