from flask import Flask, render_template, request
import rhino3dm as rh

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_model', methods=['POST'])
def generate_model():
    data = request.form['user_input']
    # send data (user input) to a service and recieve

    return render_template('model.html', data=data)

@app.route('/modify_model', methods=['POST'])
def modify_model():

    return render_template('modify_model.html')

@app.route('/modified_model', methods=['POST'])
def modified_model():

    return render_template('modified_model.html')

@app.route('/generate_gcode', methods=['POST'])
def generate_gcode():

    return render_template('gcode.html')

@app.route('/object', methods=['GET'])
def present_obj():

    return render_template('present_obj.html')

if __name__ == '__main__':
    app.run(debug=True)
