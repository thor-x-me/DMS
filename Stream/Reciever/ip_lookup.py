import socket


def get_receiver_ip():
    # Get the hostname of the local machine
    hostname = socket.gethostname()

    # Get the IP address corresponding to the hostname
    ip_address = socket.gethostbyname(hostname)

    return ip_address


if __name__ == "__main__":
    receiver_ip = get_receiver_ip()
    print(f"Receiver IP Address: {receiver_ip}")