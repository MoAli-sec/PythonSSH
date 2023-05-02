# Python SSH Command Execution

This project provides a basic implementation of executing commands over SSH using the Paramiko library. It consists of several scripts:

- ssh_cmd.py: This script demonstrates the basic idea of executing commands using Paramiko. However, before using this script, you need to ensure that the SSH service is running on your machine. But you don't need it to run the other scripts.

## Starting the SSH Service
The ssh_cmd.py script requires the SSH service to be running on your machine. Before using this script, make sure the SSH service is started. The steps to start the SSH service vary depending on the operating system:

- Linux: The SSH service is usually pre-installed on most Linux distributions. To start the service, open a terminal and run the following command:<br />
`sudo service ssh start`


- macOS: macOS also has an SSH service built-in. To start the service, open a terminal and run the following command:<br />
`sudo systemsetup -setremotelogin on`
