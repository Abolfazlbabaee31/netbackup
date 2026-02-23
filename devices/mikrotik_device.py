from .base_device import BaseDevice

class MikrotikDevice(BaseDevice):

    def get_backup(self):
        return {
            "running": self.connection.send_command("/export"),
            "version": self.connection.send_command("/system resource print"),
        }