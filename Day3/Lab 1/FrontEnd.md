To quickly set up and test the ReactJS WebSocket client in **CodeSandbox**, follow these steps:

### 1. Open CodeSandbox
Visit [CodeSandbox](https://codesandbox.io/) and select **Create Sandbox**.

### 2. Choose React Template
From the list of templates, select **React** to start with a React app.

### 3. Replace `App.js` with the Code
In the file explorer on the left:
- Open `src/App.js`.
- Replace its contents with the following code:

```jsx
import React, { useState, useEffect } from "react";

const WEBSOCKET_URL = "ws://localhost:7890"; // URL of the WebSocket server

function App() {
  const [socket, setSocket] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");

  useEffect(() => {
    // Create WebSocket connection
    const ws = new WebSocket(WEBSOCKET_URL);

    ws.onopen = () => {
      console.log("Connected to WebSocket server");
    };

    ws.onmessage = (event) => {
      // Append received messages to the list
      setMessages((prevMessages) => [...prevMessages, event.data]);
    };

    ws.onclose = () => {
      console.log("Disconnected from WebSocket server");
    };

    ws.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    setSocket(ws);

    // Cleanup on component unmount
    return () => {
      ws.close();
    };
  }, []);

  const sendMessage = () => {
    if (socket && input) {
      socket.send(input); // Send the message to the server
      setInput(""); // Clear input field
    }
  };

  return (
    <div style={{ fontFamily: "Arial, sans-serif", margin: "20px" }}>
      <h1>WebSocket Client</h1>
      <div style={{ marginBottom: "20px" }}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message"
          style={{ padding: "8px", width: "300px", marginRight: "10px" }}
        />
        <button onClick={sendMessage} style={{ padding: "8px 16px" }}>
          Send
        </button>
      </div>
      <div>
        <h2>Messages</h2>
        <ul style={{ listStyleType: "none", padding: 0 }}>
          {messages.map((message, index) => (
            <li key={index} style={{ marginBottom: "10px" }}>
              {message}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
```

### 4. Start the WebSocket Server
Run your Python WebSocket server locally on `ws://localhost:7890` using:

```bash
python your_server_file.py
```

### 5. Test the App
- Open the CodeSandbox preview window (or run locally if you downloaded the code).
- Enter messages in the input box and click **Send**.
- Confirm that the messages are echoed back and displayed in the **Messages** list.

### Notes for Running Locally:
Since CodeSandbox runs in the cloud, it may not be able to connect to your local WebSocket server (`ws://localhost:7890`). To test:
1. Download the CodeSandbox code as a ZIP file.
2. Run it locally using `npm start`.
