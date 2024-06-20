from flask import Flask, request, jsonify
import os
import google.generativeai as genai

os.environ['GOOGLE_API_KEY'] = "AIzaSyAKmoCppwSduelcRiLhx1QydgFhUtNVHaY"

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_content():
    data = request.get_json()
    query = data.get('query')
    if not query:
        return jsonify({"error": "Query not provided"}), 400

    try:
        response = model.generate_content(query)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
