import socket
import threading
import time
from Logic.Device import Device
from Logic.Player import Player
from UDPMessage import UDPMessage
from Packets.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Packets.Messages.Client.ClientInputMessage import ClientInputMessage
from Database.DatabaseManager import DataBase

class UDPServer:
    def __init__(self, host="0.0.0.0", port=5555):
        self.server_address = (host, port)
        self.clients = {}  # {client_address: {"player": Player, "battleTicks": int}}
        self.running = True
        
        # Create a UDP socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind(self.server_address)

        print(f"[✅] UDP Server started on {host}:{port}")

        # Start battle tick update loop
        self.battle_tick_thread = threading.Thread(target=self.update_battle_ticks)
        self.battle_tick_thread.daemon = True  # Auto-stops when main program stops
        self.battle_tick_thread.start()

    def update_battle_ticks(self):
        """Increase battle ticks for each connected player every 0.05s."""
        while self.running:
            for client_address, client_data in list(self.clients.items()):
                player = client_data["player"]

                try:
                    db = DataBase(player)  # ✅ Pass the correct player
                    matchmaking_data = db.loadMatchmakingData([1])[0]
                    matchmaking_data["battleTicks"] += 1
                    db.updateMatchmake(1, matchmaking_data)

                    # Send VisionUpdateMessage only if the player exists
                    byteStream = UDPMessage.encodeMessage(
                        self,
                        VisionUpdateMessage(player.device, player),
                        24109,
                        player.device
                    )
                    UDPMessage(self.server_socket, b'0123456789', client_address).send(byteStream)

                    db.connection.close()  # ✅ Close connection properly
                except Exception as e:
                    print(f"⚠️ Error updating battle ticks: {e}")

            time.sleep(0.05)

    def handle_client(self, data, client_address):
        """Process received messages and manage player connections."""
        if len(data) < 7:
            print(f"[⚠️] Received an invalid packet from {client_address}")
            return

        # If new client, register them
        if client_address not in self.clients:
            device = Device()
            player = Player(device)
            self.clients[client_address] = {"player": player, "battleTicks": 0}
            print(f"[+] New client connected: {client_address}")

        client_data = self.clients[client_address]
        player = client_data["player"]

        # Decrypt and handle the message
        message = UDPMessage.decodeMessage(self, data)
        message['payload'] = player.device.crypto.decrypt(message["payload"])

        if message["messageType"] == 10555:
            ClientInputMessage(message['payload'], player.device, player).decode()
        else:
            print(f"Skipped message from {client_address}: {message}")

        # Send VisionUpdateMessage
        byteStream = UDPMessage.encodeMessage(
            self,
            VisionUpdateMessage(player.device, player),
            24109,
            player.device
        )
        UDPMessage(self.server_socket, b'0123456789', client_address).send(byteStream)

    def start(self):
        """Main loop to receive UDP packets."""
        try:
            while self.running:
                data, client_address = self.server_socket.recvfrom(2048)  # Increased buffer size
                print(f"[🔄] Incoming data from {client_address}")
                client_thread = threading.Thread(target=self.handle_client, args=(data, client_address))
                client_thread.daemon = True  # Allows the thread to exit when the main program exits
                client_thread.start()
                
        except KeyboardInterrupt:
            print("\n[⚠️] Server shutting down...")
        finally:
            self.stop()

    def stop(self):
        """Stop the server gracefully."""
        self.running = False
        self.server_socket.close()
        print("[❌] Server stopped.")

if __name__ == "__main__":
    server = UDPServer(host="0.0.0.0", port=5555)
    server.start()
