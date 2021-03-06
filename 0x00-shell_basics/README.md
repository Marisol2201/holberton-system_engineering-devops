## 0x00. Shell, basics

**Mandatory**

- Where am I?:
  - Write a script that prints the absolute path name of the current working directory.
- Whats in there?:
  - Display the contents list of your current directory.
- There is no place like home:
  - Write a script that changes the working directory to the users home directory.
- The long format:
  - Display current directory contents in a long format
- Hidden files:
  - Display current directory contents, including hidden files (starting with .). Use the long format.
- I love numbers:
  - Display current directory contents.
- Welcome holberton:
  - Create a script that creates a directory named holberton in the /tmp/ directory.
- Betty in Holberton:
  - Move the file betty from /tmp/ to /tmp/holberton.
- Bye bye Betty:
  - Delete the file betty.
- Bye bye Holberton:
  - Delete the directory holberton that is in the /tmp directory.
- Back to the future:
  - Write a script that changes the working directory to the previous one.
- Lists:
  - Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
- File type:
  - Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
- We are symbols, and inhabit symbols:
  - Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
- Copy HTML files:
  - Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
- Lets move:
  - Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
- Clean Emacs:
  - Create a script that deletes all files in the current working directory that end with the character ~.
- Tree:
  - Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.
- Life is a series of commas, not periods:
  - Write a command that lists all the files and directories of the current directory, separated by commas (,).

**Advanced**

- File type: Holberton:
  - Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. Holberton data files always contain the string HOLBERTON at offset 0.