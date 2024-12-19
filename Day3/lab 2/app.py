from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)

# Configure the Flask app and JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a real secret key
app.config['OAUTH2_PROVIDER_TOKEN_EXPIRES_IN'] = 3600  # 1 hour

# Initialize JWT Manager and OAuth2 Provider
jwt = JWTManager(app)
oauth = OAuth2Provider(app)

# Dummy users and OAuth clients
users = {"user1": {"password": "password1", "role": "admin"}, "user2": {"password": "password2", "role": "user"}}
clients = {"client1": {"client_secret": "secret1", "redirect_uris": ["http://localhost:5000/callback"]}}

# Authentication: Login to get JWT Token
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    if username in users and users[username]["password"] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Bad username or password"}), 401

# Authorization: Restricted Resource (Admin Access)
@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    current_user = get_jwt_identity()
    if users[current_user]["role"] == "admin":
        return jsonify(message="Welcome, Admin!")
    else:
        return jsonify({"msg": "Forbidden access. Admin only."}), 403

# OAuth2.0 Authorization Endpoint
@app.route('/authorize', methods=['GET'])
@oauth.authorize_handler
def authorize():
    # You would typically use a consent page to let users authorize
    return jsonify({"msg": "OAuth authorization success"})

# OAuth2.0 Token Endpoint
@app.route('/token', methods=['POST'])
@oauth.token_handler
def access_token():
    return jsonify(message="OAuth token generated.")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000 )
