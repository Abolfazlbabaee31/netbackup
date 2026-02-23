from .base_device import BaseDevice

class CiscoDevice(BaseDevice):

    def get_backup(self):
        return {
            "running": self.connection.send_command("show running-config"),
            "startup": self.connection.send_command("show startup-config"),
            "version": self.connection.send_command("show version"),
        }