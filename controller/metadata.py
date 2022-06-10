import os
import socket
import platform

class Metadata:
    def __init__(self):
        return
        
    def print_hello_world(self):
        return f"<h1>Hello World from {self.get_hostname()} with Love!</h1>"
    
    def get_hostname(self):
        return socket.gethostname()
    
    def get_platform(self):
        return platform.platform()