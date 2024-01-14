# Command line for the win
Background Context
CMD CHALLENGE is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It’s a good training to improve your command line skills!

Requirements
General
A README.md file, at the root of the folder of the project, is mandatory
This project will be manually reviewed.
As each task is completed, the name of that task will turn green
Create a screenshot, showing that you completed the required levels
Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

Specific
In addition to completing the project tasks and submitting the required screenshots to GitHub, you are also required to demonstrate the use of the SFTP (Secure File Transfer Protocol) command-line tool to move your local screenshots to the sandbox environment.

References :

SFTP Guide
SFTP File Transfer Tutorial

Here are the steps to follow:

Take the screenshots of the completed levels as mentioned in the general requirements.
Open a terminal or command prompt on your local machine.
Use the SFTP command-line tool to establish a connection to the sandbox environment. You will need the hostname, username, and password provided to you for the sandbox environment.
Once connected, navigate to the directory where you want to upload the screenshots.
Use the SFTP put command to upload the screenshots from your local machine to the sandbox environment.
Confirm that the screenshots have been successfully transferred by checking the sandbox directory.
Once the screenshots are transferred, you can proceed to push the screenshots to GitHub as mentioned in the initial requirements.
Make sure to include the steps you followed to use the SFTP command-line tool in your project’s README.md file. This will help the reviewers understand how you performed the file transfer using SFTP.
NOTE :
The screenshoots of completed level should be inside the dir /root/alx-system_engineering-devops/command_line_for_the_win/

Manual QA Review
It is your responsibility to request a review for this project from a peer. If no peers have been reviewed, you should request a review from a TA or staff member.


## STEPS TO USE SFTP IN THE COMMAND-LINE TOOL
	- I opened command-line terminal on my local machine(might differ eg GitBash, PowerShell
	- Next, i  navigated to the sandbox(remote machine/server)
	- Copied the SFTP hostname/address
	- Pasted this command on CMD(local machine).
	- Press emter to execute command "stfp abc..."
	- If done properly, it prompts for a password which is provided by the host(ALX SANDBOX)
	- Copy and Paste or Type password. Press Enter
	- The path of CMD changes to "stfp". Showing successful connection for secure file transfer
	- At this point we have access to both local and remote machine/server at the same time
	- To access local machine hierarcy use an extra "l" for local before every shell input command
	- An example to list files in local machine will be lls instead of ls, while in the remoteit will be the normal access
	- I navigate through both running instance process of the local and remote machine using lls,lcd or ls, cd
	- When i was in both current directories that u=is dur contain my screenshot and dir where i want to transfer the screenshot to
	- I then used the put command to tranfer the file. eg "put pathto" "screenshotFileName"
	- I confirmed if it was successful by by navigating to the file i wanted it transferred to, I used ls to list files, it was transferred

