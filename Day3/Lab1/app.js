const websocket = new WebSocket("ws://localhost:8000/ws");
const messagesDiv = document.getElementById("messages");
const messageInput = document.getElementById("messageInput");

// Handle incoming messages
websocket.onmessage = function(event) {
    const message = document.createElement("div");
    message.textContent = event.data;
    messagesDiv.appendChild(message);
};

// Handle WebSocket open/close
websocket.onopen = function() {
    console.log("Connected to WebSocket server");
};

websocket.onclose = function() {
    console.log("Disconnected from WebSocket server");
};

// Send a message
function sendMessage() {
    const message = messageInput.value;
    websocket.send(message);
    messageInput.value = "";
}
