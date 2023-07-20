from loguru import logger
import time

from ..utils import generate_random_id

class Client:
    def __init__(self, host, port, protocol) -> None:
        self.host = host
        self.port = port
        self.protocol = protocol
        self.id = generate_random_id(f'{host}{protocol}')
        self.instructions = []
        self.update_last_contact_time()
        
    
    def add_instruction(self, instruction : str):
        self.instructions.append(instruction)
    
    def is_remaining_instructions(self):
        return len(self.instructions) > 0
    
    def pop_instruction(self):
        instruction = self.instructions.pop(0)
        if type(instruction) == str:
            return instruction.encode('utf-8')
        return instruction

    def update_last_contact_time(self):
        self.last_contact = int(time.time())
    
    def __str__(self) -> str:
        actual_time = int(time.time())
        diff = actual_time - self.last_contact
        return f'[{self.id}] {self.protocol}://{self.host}:{self.port} <> last contact : {diff}s'