from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os

app = Flask(__name__)
CORS(app)

# Load from environment variable or set manually
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_key_here")
client = OpenAI(api_key=OPENAI_API_KEY)

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        prompt = data.get("prompt", "")

        # Use latest SDK method
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": f"Generate a color palette for: {prompt}"}],
            max_tokens=300
        )

        content = response.choices[0].message.content

        # Sample dummy response parser
        return jsonify({
            "label": "Placeholder Palette",
            "palette": [
                { "hex": "#6A4F4B", "reason": "Earthy resilience" },
                { "hex": "#A1561C", "reason": "Fiery passion" },
                { "hex": "#DDBE99", "reason": "Warmth and calm" },
                { "hex": "#2B2D42", "reason": "Depth and mystery" },
                { "hex": "#B91C1C", "reason": "Bold statement" }
            ],
            "tags": ["resilient", "fiery", "warm", "mysterious", "bold"]
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)