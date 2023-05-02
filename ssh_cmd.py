"""
This is the basic idea of executing commands using paramiko,
but you have to enable the ssh service on your machine
"""

import paramiko


def ssh_command(ip, port, user, passwd, cmd):
    """
    Executes an SSH command on a remote server using Paramiko.

    Args:
        ip (str): The IP address of the remote server.
        port (int): The SSH port number.
        user (str): The username to authenticate with.
        passwd (str): The password for the user.
        cmd (str): The command to execute remotely.

    Returns:
        None
    """

    # Create an SSH client object
    client = paramiko.SSHClient()

    # Automatically add the server's host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    # Connect to the remote server
    client.connect(ip, port=port, username=user, password=passwd)

    # Execute the command on the remote server
    _, stdout, stderr = client.exec_command(cmd)

    # Read the command output
    output = stdout.readlines() + stderr.readlines()

    # Print the command output
    if output:
        print("--- Output ---")
        for line in output:
            print(line.strip())


if __name__ == "__main__":
    import getpass

    # Prompt the user for their username and password
    # user = getpass.getuser()
    user = input("Username: ")
    password = getpass.getpass()

    # Prompt the user for the server IP, port, and command
    ip = input("Enter server IP: ") or "192.168.1.2"
    port = input("Enter port or <CR>: ") or 22
    cmd = input("Enter command or <CR>: ") or "id"

    # Call the ssh_command function with the provided inputs
    ssh_command(ip, port, user, password, cmd)
