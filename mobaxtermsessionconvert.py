import re
import sys

def process_line(line):
    pattern = re.compile(r'(\w+)=.*?%([^%]*)%(\d{2})%.*?Interactive shell%(.*)?')

    match = pattern.search(line)

    if match:
        host = match.group(1)
        hostname = match.group(2)
        port = match.group(3)
        identity_path = match.group(4)

        identity_file = ""
        if identity_path:
            filename = identity_path.split('\\')[-1] 
            identity_file = filename.replace('.ppk', '.openssh.pub')

        print(f"Host {host}")
        print(f"    HostName {hostname}")
        print(f"    User root")
        print(f"    Port {port}")
        if identity_file:
            print(f"    IdentityFile ~/.ssh/{identity_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <input_file>")
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

