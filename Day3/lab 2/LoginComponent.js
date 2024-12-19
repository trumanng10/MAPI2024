import React, { useState } from "react";
import axios from "axios";

const LoginComponent = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [token, setToken] = useState(null);
    const [message, setMessage] = useState("");

    const handleLogin = () => {
        axios
            .post("http://localhost:5000/login", {
                username: username,
                password: password,
            })
            .then((response) => {
                setToken(response.data.access_token);
                setMessage("Login Successful!");
            })
            .catch((error) => {
                setMessage("Invalid credentials");
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
            {token && <p>Your JWT Token: {token}</p>}
        </div>
    );
};

export default LoginComponent;
