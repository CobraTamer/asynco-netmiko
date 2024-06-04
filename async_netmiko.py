import asyncio
from concurrent.futures import ThreadPoolExecutor
from netmiko import ConnectHandler

# Function to run a Netmiko command
def run_netmiko_command(device, command):
    connection = ConnectHandler(**device)
    output = connection.send_command(command)
    connection.disconnect()
    return output

# Asynchronous wrapper for the Netmiko function
async def async_netmiko_command(device, command):
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor(max_workers=1)
    return await loop.run_in_executor(executor, run_netmiko_command, device, command)
