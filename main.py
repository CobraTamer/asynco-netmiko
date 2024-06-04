
import asyncio
import yaml
from async_netmiko import async_netmiko_command

# Function to load devices from a YAML file
def load_devices(file_path):
    with open(file_path, 'r') as file:
        devices = yaml.safe_load(file)
    return devices['devices']

async def main():
    devices = load_devices('devices.yaml')
    command = 'show ip interface brief'

    # Create tasks for each device
    tasks = [async_netmiko_command(device, command) for device in devices]

    # Run tasks concurrently and gather results
    results = await asyncio.gather(*tasks)

    # Print results
    for result in results:
        print(result)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())