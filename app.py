from flask import Flask, render_template, request, send_file
from PIL import Image
import os
from io import BytesIO

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    file = request.files['file']
    if file:
        filename = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filename)
        img = Image.open(filename)
        img = img.convert('RGBA')  # Ensure image has an alpha channel

        ico_filename = filename.rsplit('.', 1)[0] + '.ico'
        img.save(ico_filename, format='ICO')
        
        return send_file(ico_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
