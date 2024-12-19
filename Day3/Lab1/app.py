import asyncio
import websockets

PORT = 7890
connected_clients = set()  # Keep track of connected clients

async def echo(websocket):
    # Register new client and log the connection
    connected_clients.add(websocket)
    print(f"New connection: {websocket.remote_address}")  # Log who connected
    try:
        async for message in websocket:
            await websocket.send(f"Echo: {message}")
            await broadcast(message)  # Broadcast the received message to all clients
    except:
        pass
    finally:
        # Unregister client and log disconnection
        connected_clients.remove(websocket)
        print(f"Disconnected: {websocket.remote_address}")  # Log who disconnected

async def broadcast(message):
    # Send message to all connected clients
    if connected_clients:  # Check if there are any clients connected
        for client in connected_clients:
            try:
                await client.send(f"Broadcast: {message}")
                print(f"Message sent to {client.remote_address}: {message}")  # Log message sent to each client
            except:
                # In case of an error sending the message (e.g., client disconnected unexpectedly)
                pass

async def main():
    print(f"Server listening on Port {PORT}")
    async with websockets.serve(echo, "0.0.0.0", PORT):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
