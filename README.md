# Flask-api-for-gemini-chatbot
This Flask API integrates the Gemini 1.5 flash model for chatbot assistance.

# Steps to Run:

1. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```
2. **Activate the Virtual Environment and install requirements:**
 
   ```bash
   venv\Scripts\activate
   ```
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the server:**

   ```bash
   python gemini.py
   ```
   
4. **Test the API:**
   
- Use a tool like Postman or send a POST request with JSON body:
  ```bash
  {
    "query": "What is the full form of AI?"
  }
  ```
- Ensure the endpoint is correct
