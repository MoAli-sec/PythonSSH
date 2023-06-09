# Python SSH Command Execution

This project provides a basic implementation of executing commands over SSH using the Paramiko library. It consists of several scripts:

- ssh_cmd.py: This script demonstrates the basic idea of executing commands using Paramiko. However, before using this script, you need to ensure that the SSH service is running on your machine. But you don't need it to run the other scripts.

## Starting the SSH Service
The ssh_cmd.py script requires the SSH service to be running on your machine. Before using this script, make sure the SSH service is started. The steps to start the SSH service vary depending on the operating system:

- Linux: The SSH service is usually pre-installed on most Linux distributions. To start the service, open a terminal and run the following command:<br>
```
sudo service ssh start
```


- macOS: macOS also has an SSH service built-in. To start the service, open a terminal and run the following command:<br>
```
sudo systemsetup -setremotelogin on
```

- Windows: Windows does not have an SSH service built-in. However, you can use third-party programs like OpenSSH or PuTTY to enable SSH functionality. You can download and install OpenSSH from the official OpenSSH website or use PuTTY as an alternative.


## Generating RSA Key Pair
The keygen.py script generates an RSA key pair (private and public keys) using the cryptography library. To generate the keys, run the keygen.py script. After running the script, you will have a private_key.pem file and a public_key.pem file.<br>
To use the generated keys with the other scripts, you need to copy the contents of the private_key.pem file and paste it into a new file named rsa_test.key. Make sure to add the RSA keyword at the start and end of the private key content in rsa_test.key.<br>

The output on the private_key.pem will be like this:<br>

```
-----BEGIN PRIVATE KEY-----
[Private Key Contents]
-----END PRIVATE KEY-----
```

You have to make it like this:<br>

```
-----BEGIN RSA PRIVATE KEY-----
[Private Key Contents]
-----END RSA PRIVATE KEY-----
````

## Client and Server Scripts
- client.py: This script implements a basic SSH client using the Paramiko library. It connects to a remote server and sends commands to execute.

- server.py: This script implements a basic SSH server using the Paramiko library. It listens for incoming SSH connections and executes the received commands.

To use the client and server scripts, you don't need to start the SSH service manually. The server script will handle the SSH server functionality, and the client script will establish a connection and send commands to execute on the server.

Please note that these scripts provide a basic implementation and may require further modifications or additional error handling for production environments.


## Usage
To use the ssh_cmd.py script, make sure the SSH service is running on your machine. Then, run the script and follow the prompts to enter the server IP, port, username, password, and command to execute remotely.

To use the client.py and server.py scripts, make sure the SSH service is not running on your machine. Run the server.py script on the machine you want to act as the SSH server. Then, run the client.py script on the machine you want to act as the SSH client. The client script will establish a connection to the server and prompt you to enter commands to execute remotely.

Note you will have to modify some lines in order for the server script to work:<br>
1- you have to change the username and password on the line 55 <br>
2- you need to add the ip of the machine you will run the server script on it <br>

In the client script you have to check the username of the server and the client machines:<br>
1- if there was the same (e.g. linux as server the username in it called moali and Windows machine the username of it is called moali) you can leave the script unchanged<br>
2- if there was not the same you have to comment line 68 and uncomment line 67 to take the username as input<br>

## Dependencies
The scripts in this project require the following dependencies:

- Python3.x

- Paramiko: You can install it using pip:<br>
```
pip install paramiko
```

- cryptography: You can install it using pip:<br>
```
pip install cryptography
```

## Disclaimer
This tool is intended for educational and testing purposes only. Please use responsibly and with the explicit permission of the remote server owner. Use them at your own risk.

## License
This project is licensed under the MIT License.

Feel free to modify and extend the code according to your needs.
