# NetBackup – Multi-Vendor Network Backup Automation Tool

NetBackup is a multi-vendor network automation tool written in Python.  
It connects to network devices via SSH, collects configuration and system information, and stores structured backups automatically.

This project is designed for lab environments, production networks, and portfolio demonstration of Network Automation skills.

---

## 🚀 Features

- Multi-vendor support (Cisco IOS, MikroTik RouterOS)
- SSH-based secure connection
- Automatic configuration backup:
  - Running configuration
  - Startup configuration (Cisco)
  - System / version information
- Structured backup directory per device & date
- Multi-threaded execution (parallel backups)
- Inventory-based device management (CSV)
- Environment variable credential support
- Logging system
- Rich CLI interface with progress visualization
- Config change comparison (Diff-ready structure)

---

## 🏗 Project Structure
