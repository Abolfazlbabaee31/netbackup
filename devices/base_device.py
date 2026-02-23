from netmiko import ConnectHandler

class BaseDevice:
    def __init__(self, ip, username, password, device_type):
        self.ip = ip
        self.username = username
        self.password = password
        self.device_type = device_type
        self.connection = None

    def connect(self):
        self.connection = ConnectHandler(
            device_type=self.device_type,
            host=self.ip,
            username=self.username,
            password=self.password,
        )

    def disconnect(self):
        if self.connection:
            self.connection.disconnect()