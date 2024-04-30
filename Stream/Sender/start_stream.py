import socket
import struct
import pickle
import cv2


def receive_video(server_ip, server_port):
    # Create a socket connection
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"Listening for incoming connections on {server_ip}:{server_port}")

    connection, address = server_socket.accept()
    client_ip = address[0]  # Get the IP address of the client

    print(f"Connection established from: {client_ip}")

    try:
        while True:
            # Receive frame size
            data = b""
            payload_size = struct.calcsize("L")  # L: unsigned long (4 bytes)
            while len(data) < payload_size:
                packet = connection.recv(payload_size - len(data))
                if not packet:
                    break
                data += packet

            if not data:
                break

            # Unpack frame size and data
            packed_msg_size = data[:payload_size]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            data = data[payload_size:]

            # Receive frame data
            while len(data) < msg_size:
                data += connection.recv(msg_size - len(data))

            # Deserialize frame
            frame = pickle.loads(data)

            # Display the received frame
            cv2.imshow("Received", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        connection.close()
        server_socket.close()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Video Streaming Program")
    parser.add_argument("--ip", required=True, help="IP address to bind the server socket")
    parser.add_argument("--port", type=int, required=True, help="Port number to bind the server socket")

    args = parser.parse_args()

    receive_video(args.ip, args.port)
