import re
import sys
import os

def process_line(line):
    # Skip headers or empty lines
    if not line.strip() or not '=' in line or line.startswith('['):
        return

    # Split the line into the host alias and its settings
    host_alias, settings_str = line.split('=', 1)
    
    # Split the settings string by the '%' delimiter
    settings = settings_str.split('%')

    # Ensure the settings list is long enough to contain necessary info
    if len(settings) < 4:
        return

    hostname = settings[1]
    port = settings[2]
    user = settings[3] if settings[3].strip() else "root" # Default to 'root' if empty

    # Don't process entries without a valid hostname (e.g., "Default Settings")
    if not hostname:
        return

    # Find the private key file (.ppk) if one is specified
    identity_path = None
    for part in settings:
        if '.ppk' in part:
            identity_path = part
            break

    # Convert the .ppk path to an OpenSSH compatible format
    identity_file = ""
    if identity_path:
        # os.path.basename is more reliable than splitting by '\\'
        filename = os.path.basename(identity_path)
        identity_file = filename.replace('.ppk', '.openssh.pub')

    # Print the formatted output
    print(f"Host {host_alias}")
    print(f"    HostName {hostname}")
    print(f"    User {user}")
    print(f"    Port {port}")
    if identity_file:
        print(f"    IdentityFile ~/.ssh/{identity_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python mobaxtermsessionconvert.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r') as file:
            for line in file:
                process_line(line.strip())
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()
