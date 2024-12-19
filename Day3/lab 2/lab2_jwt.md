Here’s a **step-by-step lab for implementing JWT authentication** using a **Python backend (Flask)** and a **React frontend** from **CodeSandbox**. This lab will cover creating a backend that generates JWT tokens and a React app that consumes the token for authentication.

---

### **Step 1: Setting up the Python Backend (Flask)**

#### 1.1 Install Dependencies

Make sure you have the following Python libraries installed:

```bash
pip install Flask Flask-JWT-Extended
```

#### 1.2 Create Flask Backend (`app.py`)

Here’s a basic Flask backend that will handle user login, JWT generation, and user authentication.

```python
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__)

# Secret key for JWT encryption
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# In-memory user data (replace with a database in production)
users = {
    "testuser": "password123"
}

# Login route to authenticate and return JWT
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    else:
        return jsonify({"msg": "Invalid credentials"}), 401

# Protected route (only accessible with JWT)
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

if __name__ == '__main__':
    app.run(debug=True,"0.0.0.0", 5000)
```

This backend has:
- A `/login` endpoint to authenticate a user and return a JWT token.
- A `/protected` endpoint that requires a valid JWT token to access.

#### 1.3 Running the Flask Backend

Run the Flask application by executing:

```bash
python app.py
```

This will start the backend at `http://localhost:5000`.

---

### **Step 2: Setting Up React Frontend in CodeSandbox**

#### 2.1 Create a New React Sandbox

Go to [CodeSandbox](https://codesandbox.io/) and create a new **React** sandbox.

#### 2.2 Install Axios for Making HTTP Requests

In the **Dependencies** section on the left side, search for `axios` and install it (or run this in your terminal if you are using a local setup):

```bash
npm install axios
```

#### 2.3 Create the React Components

- **Login Component**: This will handle user login, send credentials to the Flask backend, and store the JWT.

```jsx
// LoginComponent.js
import React, { useState } from 'react';
import axios from 'axios';

const LoginComponent = ({ setToken }) => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    const handleLogin = () => {
        axios
            .post('http://localhost:5000/login', { username, password })
            .then((response) => {
                setToken(response.data.access_token);
                setMessage('Login Successful!');
            })
            .catch((error) => {
                setMessage('Invalid credentials');
            });
    };

    return (
        <div>
            <h2>Login</h2>
            <input
                type="text"
                placeholder="Username"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
            />
            <input
                type="password"
                placeholder="Password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
            />
            <button onClick={handleLogin}>Login</button>
            <p>{message}</p>
        </div>
    );
};

export default LoginComponent;
```

- **Protected Component**: This will display protected content after the user logs in and provides the JWT.

```jsx
// ProtectedComponent.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ProtectedComponent = ({ token }) => {
    const [message, setMessage] = useState('');

    useEffect(() => {
        if (token) {
            axios
                .get('http://localhost:5000/protected', {
                    headers: { Authorization: `Bearer ${token}` },
                })
                .then((response) => setMessage(response.data.logged_in_as))
                .catch((error) => setMessage('Access Denied'));
        }
    }, [token]);

    return (
        <div>
            <h2>Protected Content</h2>
            <p>{message}</p>
        </div>
    );
};

export default ProtectedComponent;
```

- **App Component**: The main component that handles the token state and routes between the login page and the protected page.

```jsx
// App.js
import React, { useState } from 'react';
import LoginComponent from './LoginComponent';
import ProtectedComponent from './ProtectedComponent';

const App = () => {
    const [token, setToken] = useState('');

    return (
        <div>
            <h1>JWT Authentication Demo</h1>
            {!token ? (
                <LoginComponent setToken={setToken} />
            ) : (
                <ProtectedComponent token={token} />
            )}
        </div>
    );
};

export default App;
```

This setup uses:
- **LoginComponent** for login functionality.
- **ProtectedComponent** to show content based on JWT authentication.
- **App.js** to toggle between login and protected content.

#### 2.4 CORS Setup for Flask Backend

You might run into **CORS (Cross-Origin Resource Sharing)** issues since your frontend (in CodeSandbox) is hosted on a different domain than the Flask backend. To solve this, you can use Flask-CORS:

1. Install the library:

```bash
pip install flask-cors
```

2. Update `app.py` to enable CORS:

```python
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
```

This will allow your frontend to interact with your backend.

---

### **Step 3: Test the JWT Flow**

1. **Run the Flask Backend**: Start your Python backend using `python app.py`.
2. **Run the React App in CodeSandbox**: After you create the React app, it will automatically live-reload in CodeSandbox.
3. **Login**: Go to the login page in your frontend, enter the username (`testuser`) and password (`password123`), and click **Login**.
   - If successful, you'll see a message with your JWT token.
   - The frontend will then show the **protected content** by using the JWT in the `Authorization` header.

---

### **Step 4: Handling Expiration**

To handle token expiration, add the `exp` claim when creating the JWT in Flask:

```python
access_token = create_access_token(identity=username, expires_delta=False)
```

Then, when the token expires (or is invalid), the frontend should prompt the user to log in again.

---

### **Conclusion**

This simple JWT authentication flow demonstrates how to set up authentication using **Flask** as the backend and **React** for the frontend. You learned how to:
- Generate a JWT in the backend upon user login.
- Send the JWT to the frontend and store it.
- Access protected routes by sending the JWT in the request headers.
- Handle token-based authentication with React and Flask.

