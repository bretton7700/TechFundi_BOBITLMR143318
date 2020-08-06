
from flask import Flask, render_template, request
import time
import bluetooth
import os

images_FOLDER = os.path.join('static', 'images')
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = images_FOLDER


@app.route('/')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'Home.jpg')
    return render_template("homePage.html", user_image=full_filename)


@app.route('/patientDet', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


@app.route('/BtContacts')
def search():
    import time
    import bluetooth
    devices = bluetooth.discover_devices(duration=20, lookup_names=True)
    for addr, name in devices:
        return ("DeviceAddress: {0} - DeviceName: {1}".format(addr, name))
        time.sleep(6)
    # print(devices)
    #devices_dict = dict.fromkeys(devices)


@app.route('/patient', methods=['GET', 'POST'])
def patient():
    return render_template('patient.html')


if __name__ == '__main__':
    app.run(debug=True)
