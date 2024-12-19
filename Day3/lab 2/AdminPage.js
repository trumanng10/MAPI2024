import React, { useState, useEffect } from "react";
import axios from "axios";

const AdminPage = ({ token }) => {
    const [message, setMessage] = useState("");

    useEffect(() => {
        if (token) {
            axios
                .get("http://localhost:5000/admin", {
                    headers: { Authorization: `Bearer ${token}` },
                })
                .then((response) => setMessage(response.data.message))
                .catch((error) => setMessage(error.response.data.msg));
        }
    }, [token]);

    return (
        <div>
            <h2>Admin Page</h2>
            <p>{message}</p>
        </div>
    );
};

export default AdminPage;
