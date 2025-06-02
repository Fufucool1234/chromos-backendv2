
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates color palettes with explanations."},
                {"role": "user", "content": f"Generate a 5-color palette with HEX codes and reasons for each based on the prompt: '{prompt}'"}
            ]
        )

        content = response.choices[0].message.content

        # Simplified parsing for now; in production, you'd want stricter formatting
        lines = content.strip().split("\n")
        palette = []
        for line in lines:
            if "#" in line:
                parts = line.split("–")
                if len(parts) < 2:
                    parts = line.split("-")
                hex_part = parts[0].strip()
                reason = parts[1].strip() if len(parts) > 1 else "No reason provided"
                palette.append({"hex": hex_part, "reason": reason})

        return jsonify({
            "label": prompt.title(),
            "palette": palette,
            "tags": [prompt.lower()]  # Basic tag usage
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)

