import os
import datetime
from config import BACKUP_DIR
import difflib

def save_backup(hostname, data):
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    path = os.path.join(BACKUP_DIR, hostname, date)
    os.makedirs(path, exist_ok=True)

    for key, content in data.items():
        file_path = os.path.join(path, f"{key}.txt")
        with open(file_path, "w") as f:
            f.write(content)

def compare_with_previous(hostname, new_data):
    device_path = os.path.join(BACKUP_DIR, hostname)
    dates = sorted(os.listdir(device_path))
    if len(dates) < 2:
        return

    old_path = os.path.join(device_path, dates[-2], "running.txt")
    new_path = os.path.join(device_path, dates[-1], "running.txt")

    if os.path.exists(old_path):
        with open(old_path) as f1, open(new_path) as f2:
            diff = difflib.unified_diff(
                f1.readlines(),
                f2.readlines(),
                fromfile="previous",
                tofile="current",
            )
            return "".join(diff)