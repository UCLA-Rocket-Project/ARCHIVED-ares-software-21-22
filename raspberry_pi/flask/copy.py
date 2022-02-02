from flask import Flask, make_response

app = Flask(__name__)

@app.route('/<path:request>')
def handle_request(request):
    response = make_response(str(request), 200)
    response.mimetype = "text/plain"
    return response