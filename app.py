from flask import Flask, request #initialize app
from views import views
import os

app = Flask(__name__)#initialize this file. This gives us an empty website with nothing.
app.register_blueprint(views, url_prefix="/views")

UPLOAD_FOLDER = r'static\images'
app.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No image uploaded", 400
    
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    
    if file:
        # Save the file to the specified path
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return f"Image uploaded and saved as {filepath}", 200
    
    
if __name__ == '__main__':
    app.run(debug=True, port=8000)

