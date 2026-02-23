import csv
import threading
from getpass import getpass
from rich.console import Console
from rich.progress import track
from logger import setup_logger
from devices.cisco_device import CiscoDevice
from devices.mikrotik_device import MikrotikDevice
from utils import save_backup
import logging

console = Console()

def backup_device(row, username, password):
    ip = row["ip"]
    device_type = row["device_type"]

    try:
        if "cisco" in device_type:
            device = CiscoDevice(ip, username, password, device_type)
        elif "mikrotik" in device_type:
            device = MikrotikDevice(ip, username, password, device_type)
        else:
            logging.warning(f"Unsupported device: {ip}")
            return

        device.connect()
        hostname = device.connection.find_prompt().replace("#", "")
        data = device.get_backup()
        save_backup(hostname, data)
        device.disconnect()

        console.print(f"[green]✓ Backup completed for {ip}[/green]")
        logging.info(f"{ip} backup completed")

    except Exception as e:
        console.print(f"[red]✗ Failed backup for {ip}[/red]")
        logging.error(f"{ip} error: {str(e)}")

def main():
    setup_logger()

    username = input("Username: ")
    password = getpass("Password: ")

    with open("devices.csv") as file:
        reader = list(csv.DictReader(file))

    threads = []
    for row in track(reader, description="Backing up devices..."):
        t = threading.Thread(target=backup_device, args=(row, username, password))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()