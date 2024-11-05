This Python script allows users to extract password hashes from macOS user accounts. It utilizes system commands to retrieve hashed passwords securely. 

## Table of Contents 

- Project Overview
- Installation
- Usage


### Project Overview

The Mac Password Hash Extractor is designed to help users extract password hashes from macOS user accounts. This can be useful for security professionals and researchers who need to analyze password strength or recover lost passwords. The script prompts for the root password and executes a series of commands to retrieve the necessary information.
Installation
To use this script, ensure you have Python 3.x installed on your macOS system. You will also need access to the terminal.

Clone the repository:

    https://github.com/root-spidy/Password-Hashing-in-Mac.git

    cd mac-password-hash-extractor

Ensure you have the necessary permissions to run the script.

### Usage 

To run the script, execute the following command in your terminal:

`python3 extract_mac_password_hash.py`

You will be prompted to enter your root password. The script will then extract and display the password hashes for all user accounts on the system.

### Example Output

Upon successful execution, you will see output similar to this:

Hash extraction successful. 

### Output:

username1:$ml$iterations:salt:entropy

username2:$ml$iterations:salt:entropy

### Important Notes

This script requires administrative privileges.
Use this tool responsibly and only on systems you own or have explicit permission to analyze.