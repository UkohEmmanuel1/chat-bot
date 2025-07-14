from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# ✅ Your OpenRouter API Key
API_KEY = "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"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "user", "content": user_input}
        ]
    }

    try:
        res = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        res.raise_for_status()
        reply = res.json()["choices"][0]["message"]["content"]
        return jsonify({"response": reply})
    except Exception as e:
        return jsonify({"response": f"⚠️ Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
