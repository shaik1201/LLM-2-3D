from flask import Flask, request, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'obj_file' not in request.files:
        return "No file part"
    obj_file = request.files['obj_file']
    if obj_file.filename == '':
        return "No selected file"
    if obj_file and obj_file.filename.endswith('.obj'):
        filename = obj_file.filename
        obj_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return f"File {filename} uploaded successfully"
    else:
        return "Please upload a valid OBJ file"
    
@app.route('/present_obj', methods=['GET'])
def present_obj():
    return render_template('present_obj.html')

if __name__ == '__main__':
    app.run(debug=True)

