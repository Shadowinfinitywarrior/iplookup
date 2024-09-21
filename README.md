# iplookup
Track the geolocation of the given domain or ip address
# IP Lookup Tool

This is a simple Python-based IP lookup tool that works on both Kali Linux and Termux. It allows you to retrieve IP information for both domain names and IP addresses using the `ipinfo.io` API.

## Features

- Resolve domain names to IP addresses.
- Lookup IP information using an external API (`ipinfo.io`).
- Supports both IPv4 addresses and domain names.
- Can be run interactively or with a command-line argument.

## Installation

### Kali Linux

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/iplookup-tool.git
    ```

2. Navigate to the project directory:
    ```bash
    cd iplookup-tool
    ```

3. Ensure that Python3 is installed:
    ```bash
    python3 --version
    ```

4. Install the required dependencies:
    ```bash
    pip3 install requests
    ```

5. Make the script executable:
    ```bash
    chmod +x iplookup.py
    ```

6. Optionally, move the script to `/usr/local/bin` to run it from anywhere:
    ```bash
    sudo mv iplookup.py /usr/local/bin/iplookup
    ```

### Termux

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/iplookup-tool.git
    ```

2. Navigate to the project directory:
    ```bash
    cd iplookup-tool
    ```

3. Install Python3 in Termux (if not already installed):
    ```bash
    pkg install python
    ```

4. Install the `requests` library:
    ```bash
    pip install requests
    ```

5. Make the script executable:
    ```bash
    chmod +x iplookup.py
    ```

6. Optionally, move the script to your `bin` directory:
    ```bash
    mv iplookup.py $HOME/bin/iplookup
    ```

## Usage

You can run the tool in two ways:

### 1. Command-line Argument

Provide a domain or IP directly as an argument:
```bash
./iplookup.py
