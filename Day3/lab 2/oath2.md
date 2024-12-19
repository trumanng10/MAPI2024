Here's a step-by-step guide to create a simple OAuth 2.0-based application with **Python** (using **Flask**) for the backend and **ReactJS** for the frontend in **CodeSandbox**.

This tutorial will show you how to integrate **OAuth 2.0** authentication with a backend Python API and a frontend built in React.

### **Step 1: Set Up OAuth 2.0 Credentials (Google as Example)**

To begin, you'll need an OAuth 2.0 client ID and secret from a service provider (e.g., Google, GitHub, etc.). Here, we'll use **Google OAuth 2.0** as an example.

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to **APIs & Services** > **Credentials**.
4. Under **OAuth 2.0 Client IDs**, create a new client ID.
   - **Application type**: Web application.
   - Set the **Authorized Redirect URIs** to your frontend URI (e.g., `http://localhost:3000/` or in production environments, it could be something like `https://yourdomain.com/`).
5. Save the client ID and client secret, as they will be needed later.

### **Step 2: Backend - Set Up Python API with OAuth 2.0 Authentication**

1. **Create the Flask Application**

   Install Flask and the required libraries:

   ```bash
   pip install Flask Flask-OAuthlib
   ```

2. **Write the Flask Backend with OAuth 2.0**

   Create a file named `app.py`:

   ```python
   from flask import Flask, redirect, request, jsonify, session
   from flask_oauthlib.client import OAuth
   import os

   app = Flask(__name__)
   app.secret_key = os.urandom(24)

   oauth = OAuth(app)

   google = oauth.remote_app(
       'google',
       consumer_key='YOUR_GOOGLE_CLIENT_ID',
       consumer_secret='YOUR_GOOGLE_CLIENT_SECRET',
       request_token_params={
           'scope': 'email',
       },
       base_url='https://www.googleapis.com/oauth2/v1/',
       request_token_url=None,
       access_token_method='POST',
       access_token_url='https://accounts.google.com/o/oauth2/token',
       refresh_token_url=None,
       authorize_url='https://accounts.google.com/o/oauth2/auth',
   )

   @app.route('/')
   def index():
       return 'Welcome to OAuth 2.0 with Flask!'

   @app.route('/login')
   def login():
       return google.authorize(callback=url_for('authorized', _external=True))

   @app.route('/logout')
   def logout():
       session.pop('google_token')
       return redirect('/')

   @app.route('/login/authorized')
   def authorized():
       response = google.authorized_response()
       if response is None or response.get('access_token') is None:
           return 'Access denied: reason={} error={}'.format(
               request.args['error_reason'],
               request.args['error_description']
           )

       session['google_token'] = (response['access_token'], '')
       user_info = google.get('userinfo')
       return jsonify(user_info.data)

   @google.tokengetter
   def get_google_oauth_token():
       return session.get('google_token')

   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. **Explanation**:
   - `/login`: The user is redirected to Google’s authorization page.
   - `/login/authorized`: This is the callback URL, where Google redirects after authentication, sending the `access_token` back.
   - We use `Flask-OAuthlib` to integrate OAuth 2.0 and handle token retrieval and user data fetching from Google.

4. **Run Your Flask App**

   ```bash
   python app.py
   ```

   Your Flask API is now running at `http://localhost:5000/`.

---

### **Step 3: Frontend - React App in CodeSandbox**

Now let's create the React app in **CodeSandbox** and integrate it with the Python backend.

1. Go to [CodeSandbox](https://codesandbox.io/) and create a new sandbox with the **React template**.

2. In the `src` folder, create a new file `App.js` and add the following code:

   ```javascript
   import React, { useState } from "react";
   import axios from "axios";

   const App = () => {
       const [user, setUser] = useState(null);

       const handleLogin = () => {
           // Redirect to backend for Google OAuth
           window.location.href = "http://localhost:5000/login";
       };

       const fetchUser = () => {
           axios
               .get("http://localhost:5000/login/authorized")
               .then((response) => {
                   setUser(response.data);
               })
               .catch((error) => {
                   console.error("There was an error fetching the user data!", error);
               });
       };

       return (
           <div>
               <h1>OAuth 2.0 with React and Flask</h1>
               {!user ? (
                   <button onClick={handleLogin}>Login with Google</button>
               ) : (
                   <div>
                       <h2>Welcome, {user.name}</h2>
                       <img src={user.picture} alt="Profile" />
                       <p>{user.email}</p>
                       <button onClick={() => setUser(null)}>Logout</button>
                   </div>
               )}
           </div>
       );
   };

   export default App;
   ```

3. **Explanation**:
   - When the user clicks "Login with Google," they are redirected to the `/login` route of the Flask backend to begin the OAuth flow.
   - After authentication, you can call the backend to retrieve the user's data (e.g., their name, email, and picture).

4. **Install Axios** in your React sandbox to make HTTP requests:
   - In the `package.json` file, add `axios` to the dependencies:

     ```json
     {
       "dependencies": {
         "axios": "^0.27.2",
         "react": "^18.0.0",
         "react-dom": "^18.0.0",
         "react-scripts": "4.0.3"
       }
     }
     ```

---

### **Step 4: Testing the OAuth Flow**

1. **Start the Flask API** on your local machine by running:

   ```bash
   python app.py
   ```

2. **Run the React App**:
   - Since we are using CodeSandbox for the frontend, ensure the React app is running.
   
3. **Login Flow**:
   - When you click "Login with Google" on your React frontend, it will redirect you to the `/login` route of your Flask backend.
   - After logging in with Google and granting permissions, the Flask backend will redirect you back with an access token.
   - The React app will then use the `/login/authorized` endpoint to retrieve the user’s data.

---

### **Step 5: Secure and Deploy**

- **Secure Tokens**: Make sure to securely store and manage tokens in production. You might use a session or a secure HTTP-only cookie to store them.
- **Deployment**: When deploying this application, you’ll need to configure the OAuth 2.0 provider with your production URLs (backend and frontend).

---

### **Conclusion**

This lab demonstrated how to implement an OAuth 2.0 flow in a Python backend (using Flask) and a React frontend in CodeSandbox. You used Google OAuth as an example to authenticate the user and fetch their data.
