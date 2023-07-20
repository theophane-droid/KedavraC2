class c2:
    def __init__(self, host, port, freq=10, jitter=5):
        self.host = host
        self.port = port
        self.freq = freq
        self.jitter = jitter

    def __str__(self):
        return f'C2 located at {self.ip}:{self.port}'