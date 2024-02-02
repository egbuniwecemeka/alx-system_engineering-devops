# 0x08. Networking basics #1

Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is localhost/127.0.0.1
What is 0.0.0.0
What is /etc/hosts
How to display your machine’s active network interfaces

Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 20.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.7.0 via apt-get) without any errors
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing

Tasks
0. Change your home IP
mandatory
Score: 0.0% (Checks completed: 0.0%)
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

localhost resolves to 127.0.0.2
facebook.com resolves to 8.8.8.8.
The checker is running on Docker, so make sure to read this

--------------------------------------------------------------
Docker treats /etc/hosts differently. It overwrites it whenever it wants without any regard for your modifications.
To solve this you can run this workaround:

cp /etc/hosts ~/hosts.new
sed ... ~/hosts.new
cp -f ~/hosts.new /etc/hosts
You can change the sed command with that you want.
