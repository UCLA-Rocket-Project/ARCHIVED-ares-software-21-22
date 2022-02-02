import serial, time
from flask import Flask, make_response

app = Flask(__name__)
control_serial = serial.Serial("/dev/ttyACM0", 1000000)

def read_current_states():
    while not control_serial.available():
        pass
    return [int(valve) for valve in control_serial.readline().split(",")]

def actuate(next_states):
    str_next_states = next_states.join(",") + "\n"
    while read_current_states() != next_states:
        if control_serial.available():
            control_serial.print(str_next_states)
    return True

@app.route('/toggle/<path:request>')
def handle_request(request):
    next_states = read_current_states()
    for i in request.split(":"):
        next_states[int(i)] = int(not(next_states[int(i)]))
    if actuate(next_states):
        response = make_response("success", 200)
    else:
        response = make_response("fail", 200)
    response.mimetype = "text/plain"
    return response

@app.route('/fixed/<path:request>')
def handle_request(request):
    for _ in range(2):
        control_serial.print(request)
    response = make_response("done", 200)
    response.mimetype = "text/plain"
    return response