from flask import Flask, make_response, send_file
import serial

port = '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.4:1.0'
app = Flask(__name__)

while True:
    try:
        print('hello')
        serial_port = serial.Serial(port, 9600, timeout=0.1)
    except:
        continue
    finally:
        break

@app.route('/favicon.ico')
def favicon():
    return ('', 200)

@app.route('/<path:request>')
def handle_request(request):
    response = make_response('failure', 200)
    serial_request = 'S' + request + 'E\n'
    for _ in range(5):
        try:
            serial_port.write(serial_request.encode())
            serial_response = serial_port.readline()
        except:
            serial_port = serial.Serial(port, 9600, timeout=0.1)
            continue
            
        try:
            serial_response = serial_response.decode()
        except:
            continue

        if (serial_response == serial_request):
            response = make_response('success', 200)
            break

    response.mimetype = 'text/plain'
    return response

"""
@app.route('/download/<path:filename>')
def download_file(filename):
    file = '/home/ubuntu/logs/' + filename
    return send_file(file, as_attachment=True)
"""