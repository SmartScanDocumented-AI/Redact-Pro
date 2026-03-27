from flask import Flask, request, send_file, after_this_request
from flask_cors import CORS  
import os
from masker import process_image

app = Flask(__name__)

# This allows your frontend (port 8000) to safely talk to this backend (port 5000)
CORS(app, resources={r"/upload": {"origins": "http://127.0.0.1:8000"}})

UPLOAD_FOLDER = "uploads"
RESULTS_FOLDER = "results"

# Ensure both directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULTS_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_file():
    # 1. Check if file part is in request
    if 'file' not in request.files:
        return {"error": "No file uploaded"}, 400

    file = request.files['file']
    if file.filename == '':
        return {"error": "No selected file"}, 400

    # 2. Save uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # 3. Read mask mode from the frontend form (black/blur/highlight)
    mode = request.form.get("mode", "black") 

    # 4. Process the image
    try:
        # Calls the function in masker.py
        masked_image_path = process_image(filepath, mode)
        
        if not masked_image_path or not os.path.exists(masked_image_path):
            raise Exception("Masking failed - output file not created.")

        # Cleanup: Remove the ORIGINAL uploaded file after the response is sent
        @after_this_request
        def cleanup(response):
            try:
                if os.path.exists(filepath):
                    os.remove(filepath)
            except Exception as e:
                print(f"Error during cleanup: {e}")
            return response

        # 5. Return the masked image
        # Note: mimetype is set to image/png or image/jpeg as needed
        return send_file(masked_image_path, mimetype='image/png')

    except Exception as e:
        # This will show up in your Python terminal for debugging
        print(f"Backend Error: {e}") 
        return {"error": str(e)}, 500

if __name__ == "__main__":
    # We use Port 5000 to avoid conflict with your Port 8000 frontend
    app.run(host="127.0.0.1", port=5000, debug=True)