 Async Netmiko

This project provides an asynchronous wrapper for Netmiko to enable parallel execution of commands on network devices.

## Files

- `async_netmiko.py`: Contains the asynchronous wrapper for Netmiko commands.
- `main.py`: Demonstrates how to use the asynchronous Netmiko wrapper.
- `devices.yaml`: Contains the inventory of network devices.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/CobraTamer/async-netmiko.git
    cd async-netmiko
    ```

2. Install the required Python packages:
    ```bash
    pip install netmiko asyncio pyyaml
    ```

## Usage

1. Modify the `devices.yaml` file with your network devices and credentials.

2. Run the script:
    ```bash
    python main.py
    ```

## Example Output

When you run the script, you should see the output of the `show ip interface brief` command for each device listed in the `devices.yaml` file.
