
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/generate": {"origins": "*"}})

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        # Placeholder logic (this would be replaced by actual LUMA engine output)
        palette = [
            {"hex": "#6A4F4B", "reason": "Earthy resilience"},
            {"hex": "#A1561C", "reason": "Fiery passion"},
            {"hex": "#DDBE99", "reason": "Warmth and calm"},
            {"hex": "#2B2D42", "reason": "Depth and mystery"},
            {"hex": "#B91C1C", "reason": "Bold statement"},
        ]
        tags = ["resilient", "fiery", "warm", "mysterious", "bold"]

        return jsonify({"label": "Placeholder Palette", "palette": palette, "tags": tags})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
