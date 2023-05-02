# importing libraries
import paramiko
import shlex
import subprocess

def ssh_command(ip, port, user, passwd, command):
    """
    Establishes an SSH connection to a remote server and executes a command.
    :param ip: The IP address of the remote server.
    :param port: The port number for the SSH connection.
    :param user: The username for the SSH connection.
    :param passwd: The password for the SSH connection.
    :param command: The command to execute on the remote server.
    """
    # Create an SSH client object
    client = paramiko.SSHClient()

    # Automatically add the server's host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the remote server
    client.connect(ip, port=port, username=user, password=passwd)

    # Create an SSH session
    ssh_session = client.get_transport().open_session()

    # Check if the session is active and send the command
    if ssh_session.active:
        ssh_session.send(command)

        # Receive and print the command output
        print(ssh_session.recv(1024).decode())

        # Keep receiving commands until the user types 'exit'
        while True:
            command = ssh_session.recv(1024)
            try:
                cmd = command.decode().strip()
                if cmd == 'exit':
                    # Close the SSH connection when the user types 'exit'
                    client.close()
                    break
                elif cmd:
                    # Execute the command and send the output back to the client
                    cmd_output = subprocess.check_output(shlex.split(cmd), shell=True)
                    ssh_session.send(cmd_output or 'okay')
                else:
                    # If the command is empty, ignore it and continue
                    continue
            except Exception as e:
                # Send any exceptions raised to the client
                ssh_session.send(str(e))

            finally:
                print("ok")
                continue

        # Close the SSH connection
        client.close()
    return

if __name__ == "__main__":
    import getpass

    # Get the current user and password
    # If the username of the server and client machines is diffrente you should use this instead
    # user = input("Username: ")
    user = getpass.getuser()
    password = getpass.getpass()

    # Get the server IP address and port number from the user
    ip = input('Enter server IP: ')
    port = input('Enter port: ')

    # Connect to the server and send the 'ClientConnected' command
    ssh_command(ip, port, user, password, 'ClientConnected')
