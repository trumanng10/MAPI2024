from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/json")
def home():
    sender_ip = request.remote_addr  # Captures the IP of the requester
    cookies = request.cookies  # Retrieves cookies sent with the request
    return jsonify(
        message="Hello, Flask running inside Docker!",
        SenderIP=sender_ip,
        HeaderFormat="JSON",
        Cookies=cookies  # Include cookies in the response
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
