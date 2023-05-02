# importing libraries
import os
import paramiko
import socket
import sys
import threading

# Get the current working directory
CWD = os.path.dirname(os.path.realpath(__file__))

# Load the RSA key from the specified file
HOSTKEY = paramiko.RSAKey(filename=os.path.join(CWD, 'test_rsa.key'))


class Server(paramiko.ServerInterface):
    """
        Custom ServerInterface implementation.

        This class provides the interface for handling SSH server events and authentication.

        Attributes:
            event (threading.Event): An event object used for synchronization.
        """
    def __init__(self):
        self.event = threading.Event()

    def check_channel_request(self, kind, chanid):
        """
        Check if the channel request is allowed.

        Args:
            kind (str): The type of the channel request.
            chanid: The channel ID.

        Returns:
            int: OPEN_SUCCEEDED if the request is allowed, OPEN_FAILED_ADMINSTRATIVELY_PROHIBITED otherwise.
        """
        # Allow only session channel requests
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINSTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        """
        Check if the provided username and password are valid for authentication.

        Args:
            username (str): The username to check.
            password (str): The password to check.

        Returns:
            int: AUTH_SUCCESSFUL if the authentication is successful, otherwise None.
        """
        # Check if the provided username and password match
        if (username == "wanheda") and (password == "omnia35"):
            return paramiko.AUTH_SUCCESSFUL


if __name__ == "__main__":
    server = '192.168.1.2'
    ssh_port = 2222
    try:
        # Create a socket and bind it to the server and port
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
        print("[+] Listening for connection ...")
        client, addr = sock.accept()
    except Exception as e:
        print('[-] Listen failed: ' + str(e))
        sys.exit(1)
    else:
        print("[+] Got a connection!", client, addr)

    # Create a new paramiko.Transport object with the client socket
    bhSession = paramiko.Transport(client)

    # Add the server's RSA key to the transport
    bhSession.add_server_key(HOSTKEY)

    # Create an instance of the custom Server class
    server = Server()

    # Start the SSH server
    bhSession.start_server(server=server)

    # Accept a new SSH channel
    chan = bhSession.accept(20)
    if chan is None:
        print('*** No channel.')
        sys.exit(1)

    print('[+] Authenticated!')
    print(chan.recv(1024))
    chan.send("Welcome to mo_ssh")
    try:
        while True:
            # Taking commands from the user to execute
            command = input("Enter command: ")
            if command.strip() == '':
                continue  # Skip the loop iteration if the command is empty
            if command != 'exit':
                # Send the command to the SSH channel
                chan.send(command)
                r = chan.recv(8192)
                print(r.decode())
            else:
                chan.send('exit')
                print('Exiting')
                bhSession.close()
                break
    except KeyboardInterrupt:
        bhSession.close()
